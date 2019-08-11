DOC_NAME 	 = main

all::
	latexmk -pdf ${DOC_NAME}.tex

view: $(DOC_NAME).pdf
	xdg-open $(DOC_NAME).pdf

clean::
	rm -fv *.nav *.fls *.fdb_latexmk *.snm *.aux *.log *.bbl *.blg *.toc *.out *.lot *.lof $(DOC_NAME).pdf
	