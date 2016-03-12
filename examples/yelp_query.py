# -*- coding: utf-8 -*-

import json
import pprint
import sys
import urllib
import urllib2
import os
import pdb

import oauth2


API_HOST = 'api.yelp.com'
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'Campbell, CA'
SEARCH_LIMIT = 5
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'

# OAuth credential placeholders that must be filled in by users.
CONSUMER_KEY = os.environ.get('YELP_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('YELP_CONSUMER_SECRET')
TOKEN = os.environ.get('YELP_TOKEN')
TOKEN_SECRET = os.environ.get('YELP_TOKEN_SECRET')


def request(host, path, url_params=None):
    """Prepares OAuth authentication and sends the request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = 'http://{0}{1}?'.format(host, urllib.quote(path.encode('utf8')))

    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request(method="GET", url=url, parameters=url_params)

    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    print u'Querying {0} with params {1}...'.format(url, url_params)

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response


def search(term, location):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, url_params=url_params)


def get_business(business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path)


def query_api(term, location):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(term, location)
    # response contains ['region', 'total', 'businesses']

    businesses = response.get('businesses')
    # ['is_claimed', 'rating', 'mobile_url', 'rating_img_url', 'review_count',
    # 'name', 'rating_img_url_small', 'url', 'is_closed', 'phone', 'snippet_text',
    # 'image_url', 'categories', 'display_phone', 'rating_img_url_large', 'id',
    # 'snippet_image_url', u'location']

    if not businesses:
        print u'No businesses for {0} in {1} found.'.format(term, location)
        return

    for business in businesses:
        # business_id = business['id']
        # response = get_business(business_id)

        print('----- {} -----'.format(business['name']))
        print('    {}'.format(business['url']))
        print('    {}'.format(business['categories']))

    # pprint.pprint(response, indent=2)


def main():

    try:
        r = query_api('italian', 'campbell, ca')
        print('results are:')
        print(r)
    except urllib2.HTTPError as error:
        sys.exit('Encountered HTTP error {0}. Abort program.'.format(error.code))


if __name__ == '__main__':
    main()