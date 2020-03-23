# tex2plaintxt
## Motivation & Overview
When writing a paper in English, I use [Grammarly](https://grammarly.com/). However, the web editor of Grammarly supports only plain texts so that Grammarly does not recognize LaTeX macro. In writing a paper, I use macros to fix vocabulary.

This repository includes scripts for converting the LaTeX file to plan text with expanding macro. After converting with `latex2plain.py`, you can copy & paste the plain text to the web editor of Grammarly. When finishing editing on web editor, `plain2latex.py` converts the fixed plan text to latex.

## Enviroment
- Python 3.6.5
## Usage
- Convert LaTeX to Text
    - output file name for `hoge.tex` is `hoge.txt` 
```
python latex2plain.py $PATH_TO_LATEX_FILE
```
- Convert Text to LaTeX
```
python plain2latex.py $PATH_TO_LATEX_FILE
```

## License
WTFPL

