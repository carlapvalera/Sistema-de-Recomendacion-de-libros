import json
import imports

proces = imports.Proces(root = "C:\\blabla\\sriii\\recommend-books\\input")

print(proces.import_txt_files())
proces.title_text(proces,proces.import_txt_files(proces))

