from jira import JIRA

jira = JIRA('https://jira-hdd.wdc.com')
# auth_jira = JIRA(auth=('username', 'password'))
# auth_jira = JIRA(auth=('Akihiro.Kamimura@wdc.com', 'wdc04Kami'))


# all values are samples and won't work in your code!
key_cert_data = None
with open(key_cert, 'r') as key_cert_file:
  key_cert_data = key_cert_file.read()

oauth_dict = {
    'access_token': 'foo',
    'access_token_secret': 'bar',
    'consumer_key': 'jira-oauth-consumer',
    'key_cert': key_cert_data
}
auth_jira = JIRA(oauth=oauth_dict)
