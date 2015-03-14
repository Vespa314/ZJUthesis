latex --src-specials --synctex=-1 毕业论文
makeindex 毕业论文.idx
bibtex 毕业论文
latex --src-specials --synctex=-1 毕业论文
latex --src-specials --synctex=-1 毕业论文
dvipdfmx -p a4 毕业论文

del *.out
del *.log
del *.idx
del *.ilg
del *.ind
del *.lof
del *.aux
del *.dvi
del *.lot
del *.toc
del *.blg
del *.bbl
del *.synctex
del .\Chapters\*.aux