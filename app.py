from flask import Flask, render_template, flash, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from tone_analyser import analyzeTone
from exclamation import exclamationFunc
from qualifier import qualifierFunc
from thanks import thanksFunc
from cautious import cautiousFunc
from apologise import apologiseFunc

app = Flask(__name__, template_folder='template')

app.config['SECRET_KEY'] = "mysecretkey"

class ToneAnalyzerForm(FlaskForm):
	message = TextAreaField(render_kw={"placeholder": "Paste your email text here!"})
	submit = SubmitField('analyze')

@app.route("/recommend", methods=['GET', 'POST'])
def recommend():
	message = '';
	return render_template('recommend.html')

@app.route("/analyze", methods=['GET', 'POST'])
def analyze():
	form = request.form
	message = form.message.data

	if form.validate_on_submit():
		return render_template('recommend.html', message=message)
	else:
		scores, tones = analyzeTone(message)
		form.message.data = ''
	return render_template('analyze.html', form=form, message=message, scores=scores, tones=tones)
	

@app.route("/index", methods=['GET', 'POST'])
def index():

	form = ToneAnalyzerForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			action = request.form['action']
			if action == 'analyze':
				scores, tones = analyzeTone(form.message.data)
				message = form.message.data
				return render_template('analyze.html', form=form, message=message, scores=scores, tones=tones)
			if action == 'recommend':
				message = form.message.data
				return recommendTones(message)
	return render_template('welcome.html', form=form)

def recommendTones(message):
	apologies = ["sorry", "apologise", "apologies", "hope it's not too late"]
	apologytext = """Wow, you must be really sorry! You apologised an entire %d times in your email. Unless you accidentally ran over your supervisor's puppy, that's really not necessary."""


	cautious =  ["would you mind", "do you think", "would it be possible", "if it’s no bother", "no worries", "if it’s okay", 
			"if you don’t mind", "too inconvenient", "don't worry if not"]
	cautioustext = """You seem pretty hesistant in your email - you've used %d phrases that indicate you're worried to inconvenience the recipient. Just ask Thomas for that report he owes you, he's three days late already!"""

	qualifiers = ['just', 'actually', "anyway", "not sure", "not certain", "not an expert", 
			  "no expert", "anyways", "not sure, but", "i think", "i feel"]
	qualifiertext = """Qualifiers are words like 'just' and 'actually' and phrases like 'I'm not an expert, but...' that undermine what you're saying before you've even said it. You're using %d of them, oh my. Get rid of them - you know what you're talking about."""
   
	punct = ["!"]
	puncttext = "You've used %d exclamation marks. Did you know that exclamation marks are often only used to appear friendlier? Unless you are genuinely excited, please delete some."

	thanks = ["thank", "really appreciate it", "grateful"]
	thankstext = """Did someone save your life at great personal expense? You decided to thank the recipient of this email %d times. One thank you is usually enough - can you pick your favourite and remove the others?"""

	apologiesResult = apologiseFunc(apologies, message, apologytext)
	cautiousResult = cautiousFunc(cautious, message, cautioustext)
	qualifierResult = qualifierFunc(qualifiers, message, qualifiertext)
	puncResult = exclamationFunc(punct, message, puncttext)
	thanksResult = thanksFunc(thanks, message, thankstext)

	return render_template('recommend.html', message=message, appologiesResult=apologiesResult, cautiousResult=cautiousResult, qualifierResult=qualifierResult, puncResult=puncResult, thanksResult=thanksResult)

if __name__ == "__main__":
	app.debug = True
	app.run()