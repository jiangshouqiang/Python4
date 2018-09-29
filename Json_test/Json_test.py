import json
d = dict(name="bob",age=20,score=99,test_null=None)
print(json.dumps(d))

json_str = '{"test_null": null, "age": 20, "name": "bob", "score": 99}'
print(json.loads(json_str))

str = ''
print((str is ''))

obj = {'matchConcede': '受半球',
 'matchGuestIcon': 'http://img.zgzcw.com/zgzcw/matchCenter/team/images/2013121192235.png',
 'matchGuestName': '谢菲联',
 'matchHomeTeamIcon': 'http://img.zgzcw.com/zgzcw/matchCenter/team/images/2013121205249.png',
 'matchHomeTeamName': '伯顿',
 'matchLeagueIcon': 'http://img.zgzcw.com/zgzcw/matchCenter/league/images/20130118142426.jpg',
 'matchLeagueName': '英冠',
 'matchTime': '2017-11-18 03:45'}

print(json.dumps(obj))