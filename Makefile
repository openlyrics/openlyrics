.PHONY: all
all: well-formed validate

.PHONY: well-formed
well-formed: examples/*.xml songs/*.xml
	@for file in examples/*.xml songs/*.xml; \
		do \
			echo "Checking..." "$$file"; \
			xmllint --noout "$$file"; \
		done

.PHONY: validate
validate: examples/*.xml songs/*.xml
	@for file in examples/*.xml songs/*.xml; \
		do \
			if grep -q 'version="0.8"' "$$file"; \
			then \
				echo -n "Validating (0.8)... " && \
				xmllint \
					--noout \
					--relaxng openlyrics-0.8.rng \
					"$$file"; \
			fi; \
		done

.PHONY: help
help:
	@echo "Targets:"
	@echo "  all         - Perform all operations"
	@echo "  well-formed - Checks that transforming XSL and XML are well formed"
	@echo "  validate    - Validates OpenLyrics XML files against RelaxNG scheme"
