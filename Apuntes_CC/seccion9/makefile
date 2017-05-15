# Makefile local
TEX = pdflatex -shell-escape -interaction=nonstopmode -file-line-error
ASY= asy
all: main.pdf

main.pdf : main.tex
	$(TEX) main.tex
	rm -rf *.aux *.log *.out

main.figs : *.asy
	$(ASY) *.asy

clean:
	rm -rf *.log *.aux *.pdf *.blg *.bbl *.synctex.gz *.dvi
