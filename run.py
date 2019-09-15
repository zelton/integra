import os
from datetime import datetime

import bitbucket.auth
import bitbucket.pull_requests
import slack

bitbucket.auth.prepare_token()

repos = os.getenv('BITBUCKET_REPOSITORIES').split(';')
text = ''
text += '%s\n' % datetime.now().strftime("%d.%m.%Y %H:%M")
counter = 0
for repo in repos:
    text += '<%s|*%s*>\n' % ('https://bitbucket.org/%s/pull-requests/' % repo, repo)
    prs = bitbucket.pull_requests.pull_requests_to_review(repo)
    counter += len(prs)
    for pr in prs:
        text += ':white_small_square: <%s|%s>\n' % (pr['href'], pr['title'])
    text += '\n'

if counter > 0:
    slack.message(text)
