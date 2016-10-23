mkdir -p ../output
python code_130010048.py

pdflatex report_130010048.tex
biblatex report_130010048.aux
pdflatex report_130010048.tex
pdflatex report_130010048.tex

mv report_130010048.pdf ../output/

mv voltage_across_elements_in_under_damped_case.mp4 ../output/
mv voltage_across_elements_in_critically_damped_case.mp4 ../output/
mv voltage_across_elements_in_over_damped_case.mp4 ../output/

jupyter nbconvert --execute --to html project1_130010048.ipynb

rm *.png

mv project1_130010048.html ../output/

rm *.aux *.log *.out *.bbl *.blg
