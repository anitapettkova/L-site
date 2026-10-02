.PHONY: install-hugo run vale-sync vale-test push
.DEFAULT_GOAL := help

install-hugo: ## Install hugo
	brew install hugo

run: ## Run hugo server
	hugo server -D --gc

vale-sync: ## Sync vale configs
	vale sync
	
vale-test: ## Run vale test on all `md` files
	find . -iname "*.md" -exec vale {} \;

push: ## Push changes to git
	ssh-add ~/.ssh/id_rsa
	git add .
	git commit -m "Pushing changes automatically for Anita"
	git push

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
