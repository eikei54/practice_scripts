import base64


def base64_to_str(x):
  """base64表現を文字列に変換する
  b64decode() はbytesであるため
 文字列はdencode()で文字列にして渡す
  """
  return base64.b64decode(x).decode('utf-8')


def main():
  target = sys.argv[1]
  print(base64_to_str(target))


# if __name__ == "__main__":
#  main()

__all__ = ['base64_to_str']
