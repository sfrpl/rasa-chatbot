help:
	@echo "    train"
	@echo "        Train a stacked model using Rasa Core and NLU."
	@echo "    run-core"
	@echo "        Spin up the core server on the command line"
	@echo "    run-actions"
	@echo "        Spin up the action server"
	@echo "    run"
	@echo "        Spin up both core and the action server"
	@echo "    visualize"
	@echo "        Show your stories as a graph"

run:
	make run-actions&
	make run-core

run-core:
	rasa run --verbose --endpoints endpoints.yml --credentials credentials.yml --cors "*"

	
run-core-debug:
	rasa run --verbose --endpoints endpoints.yml --credentials credentials.yml --debug --cors "*"

	
run-actions:
	rasa run actions


train-nlu:
	rasa train nlu --config config.yml -u data/nlu_data/
	
train-core:
	rasa train core -d domain.yml -s data/stories.md --out models -c config.yml


train-interactive:
	rasa interactive --verbose --endpoints endpoints.yml

visualize:
	rasa show stories