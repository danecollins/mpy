https://slack.com/api/chat.postMessage?token=xoxp-4002768743-4006228863-4166574522-c2c0a4&channel=%23log&text=First%20log%20message&username=danecollins&pretty=1

pip install git+git://github.com/loisaidasam/pyslack.git


>>> import logging
>>> from pyslack import SlackHandler

>>> logger = logging.getLogger('test')
>>> logger.setLevel(logging.DEBUG)

>>> handler = SlackHandler('YOUR-TOKEN-HERE', '#channel_name', username='botname')
>>> handler.setLevel(logging.WARNING)
>>> formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s (%(process)d): %(message)s')
>>> handler.setFormatter(formatter)
>>> logger.addHandler(handler)

>>> logger.error("Oh noh!") # Will post the formatted message to channel #channel_name from use