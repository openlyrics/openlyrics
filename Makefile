.PHONY: all
all: well-formed validate convert-09-08

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
			elif grep -q 'version="0.9"' "$$file"; \
			then \
				echo -n "Validating (0.9)... " && \
				xmllint \
					--noout \
					--relaxng openlyrics-0.9.rng \
					"$$file"; \
			fi; \
		done

.PHONY: convert-09-08
convert-09-08: songs/*.xml
	@mkdir -p export-openlyrics-0.8
	@rm -f export-openlyrics-0.8/*.xml
	@echo "Deleting export-openlyrics-0.8/*.xml files"
	@for file in examples/*.xml songs/*.xml; \
		do \
			if grep -q 'version="0.9"' "$$file"; \
			then \
				echo -n "Converting to OpenLyrics 0.8... $$file\n" && \
				name=$${file##*/} && \
				xsltproc \
					--output export-openlyrics-0.8/"$$name" \
					tools/openlyrics-0.9-to-openlyrics-0.8.xsl \
					"$$file"; \
			fi; \
		done
	@for file in export-openlyrics-0.8/*.xml; \
		do \
			xmlformat --in-place --config-file=tools/xmlformat.conf "$$file"; \
			sed --in-place --regexp-extended ':a;N;$$!ba;s/\r{0,1}\n\s+<br\s*\/*>/<br\/>/g' "$$file"; \
		done
	@for file in export-openlyrics-0.8/*.xml; \
		do \
			echo -n "Validating... " && \
			xmllint \
				--noout \
				--relaxng openlyrics-0.8.rng \
				"$$file"; \
		done

.PHONY: convert-08-09
convert-08-09: songs/*.xml
	@echo "Converting schema from 0.8 to 0.9 for song/*.xml files"
	@for file in songs/*.xml; \
		do \
			if grep -q 'version="0.8"' "$$file"; \
			then \
				echo -n "Converting schema to OpenLyrics 0.9... $$file\n" && \
				name=$${file##*/} && \
				xsltproc \
					--output songs/"$$name" \
					--param empty-chords "true()" \
					--stringparam chord-notation english \
					--stringparam xmllang en \
					--param remove-optional "true()" \
					--param update-meta "false()" \
					--param add-pi "false()" \
					tools/openlyrics-0.8-to-openlyrics-0.9.xsl \
					"$$file"; \
			fi; \
		done
	@for file in songs/*.xml; \
		do \
			xmlformat --in-place --config-file=tools/xmlformat.conf "$$file"; \
			sed --in-place --regexp-extended ':a;N;$$!ba;s/\r{0,1}\n\s+<br\s*\/*>/<br\/>/g' "$$file"; \
		done
	@for file in songs/*.xml; \
		do \
			echo -n "Validating... " && \
			xmllint \
				--noout \
				--relaxng openlyrics-0.9.rng \
				"$$file"; \
		done

.PHONY: help
help:
	@echo "Targets:"
	@echo "  all           - Perform all default operations"
	@echo "  well-formed   - Checks that transforming XSL and XML are well formed"
	@echo "  validate      - Validates OpenLyrics XML files against RelaxNG scheme"
	@echo "  convert-09-08 - Converts OpenLyrics 0.9 files to OpenLyrics 0.8"
	@echo "  convert-08-09 - Converts OpenLyrics 0.8 files to OpenLyrics 0.9"
