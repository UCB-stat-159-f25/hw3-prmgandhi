.PHONY: env
env:
	@echo ">>> Setting up or updating conda environment: ligo"
	@if conda env list | grep -q "ligo"; then \
		echo "Environment exists -> updating"; \
		conda env update -f environment.yml --name ligo --prune; \
	else \
		echo "Creating new environment"; \
		conda env create -f environment.yml; \
	fi
	@echo "Environment setup complete."

.PHONY: html
html:
	@echo ">>> Building HTML documentation with MyST"
	myst build --html
	@echo ">>> Build complete. View the output locally in _build/html."

.PHONY: clean
clean:
	@echo ">>> Cleaning up generated files"
	rm -rf _build/* figures/* audio/*
	@echo ">>> Clean complete."
