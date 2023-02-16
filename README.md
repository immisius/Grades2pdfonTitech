# Grades2pdfonTitech
東京工業大学の成績表をpdfあるいはcsvに変換するプログラムです。
担当教師欄を無くしたいモチベーションの元、作成されました。

成績のページで右クリックをして検証、あるいはページのソースを表示より、htmlデータをコピーしてください。そして
`grade.html`ファイルを作成しその中にペーストしてください

# make csv
```
pip install -r requirements.txt
python to_csv.py
```
# make pdf
wkhtmltopdfが必要になります。
https://laboratory.kazuuu.net/creating-a-pdf-from-html-in-python-using-pdfkit/
を参考にインストールしてください
```
pip install -r requirements.txt
python to_pdf.py
```
