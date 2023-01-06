DOC = am205_hw0
LATEXMK = latexmk

default: $(DOC).pdf

$(DOC).pdf: $(DOC).tex
	$(LATEXMK) -pdf $< || $(RM) $@

mostlyclean:
	$(LATEXMK) -silent -c -f
	$(RM) *.bbl *-blx.bib *.fff

clean: mostlyclean
	$(LATEXMK) -silent -C -f
	$(RM) *.run.xml *.synctex.gz
	$(RM) *.d

.SUFFIXES:
.PHONY: default $(DOC).pdf
