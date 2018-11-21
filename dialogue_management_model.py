from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import rasa_core
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application
from bot_server_channel import BotServerInputChannel
from rasa_core.policies.form_policy import FormPolicy
from rasa_core.featurizers import (
    MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer)

#from rasa_addons.webchat import WebChatInput, SocketInputChannel
logger = logging.getLogger(__name__)

def run_chat_bot(serve_forever=True):
	interpreter = RasaNLUInterpreter('./models/nlu/default/hospnlu')
	action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
	agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)
	channel = BotServerInputChannel(agent)
	agent.handle_channels([channel])
	input_channel = WebChatInput(static_assets_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static'))
	agent.handle_channel(SocketInputChannel(5500, "/bot", input_channel))
	#rasa_core.run.serve_application(agent ,channel='cmdline')
		
	return agent

	
if __name__ == '__main__':
	run_chat_bot()