PANDOC = pandoc
META = quiz.yaml

all: \
	am205_quiz1.pdf \
	am205_quiz1_sol.pdf \
	am205_quiz2.pdf \
	am205_quiz2_sol.pdf \
	am205_quiz3.pdf \
	am205_quiz3_sol.pdf \
	am205_quiz4.pdf \
	am205_quiz4_sol.pdf \

am205_quiz1.pdf: q7_cheb_equi.pdf

q7_cheb_equi.pdf: q7_cheb_equi.py
	./$<

%.pdf: %.md
	$(PANDOC) --metadata-file $(META) "$<" -o "$@"

clean:
	rm -vf *.pdf *.html

.PHONY: all clean
.SUFFIXES: .md .pdf .html
