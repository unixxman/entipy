from sqla_examples.transactions.direct_connection_use import direct_connection_use

def test_direct_connection_use():
  val, = direct_connection_use()
  assert val == 1