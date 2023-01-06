DOC = am205_hw4
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
	$(RM) $(DOC)_md.pdf $(DOC).html

.SUFFIXES:
.PHONY: default $(DOC).pdf
