from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'hospnlu')
	
def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/hospnlu')
	txt="Please schedule an appointment with oncology dept"
	output=interpreter.parse(u"schedule an appointment cool guy with oncology dept")
	
	for op in output.keys():
		print (op,':',output[op])
		if op=='entities':
			for d in (output[op]):
				if d['extractor']=='ner_duckling_http':
					time_slot=d['value']
					date = time_slot[0:10]
					time = time_slot[11:19]
					print(date,time)
	
	
if __name__ == '__main__':
	train_nlu('./data/data.json', 'config.yml', './models/nlu')
	run_nlu()