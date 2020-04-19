import pathlib


items = (
  pathlib.Path('hoge\\foo'),
  pathlib.Path('hoge\\bar'),
)


my_path = 'C:\\fw\\ip'

print(items)

for _ in items:
    t = my_path / _
    print(t)

