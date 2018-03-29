"# chatbot" 

https://chatbotslife.com/build-simple-chatbot-with-rasa-part-1-f4c6d5bb1aea

Need to run "conda install spacy"

rasa-nlu-trainer -v data/training_data.json

Issue installing:
	Cannot install Twisted
		https://dimitri.janczak.net/2017/05/20/python-3-6-visual-studio-2017/
		https://wiki.python.org/moin/WindowsCompilers
	
	python -m spacy download en
		Error: Couldn't link model to 'en'
		Run as admin
		
	ModuleNotFoundError: No module named 'rasa_core'
		