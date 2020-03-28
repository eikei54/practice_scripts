class Klass:
  def __new__(cls, *args):  # コンストラクタ
    print(f'{cls=}')
    print('new', args)
    # 作成したインスタンスを返す
    return super().__new__(cls)

  def __init__(self, *args):
    # インスタンスの初期化はこちらで行う
    print('init', args)


kls = Klass(1, 2, 3)
