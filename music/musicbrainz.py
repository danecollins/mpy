# To experiment with this code freely you will have to run this code locally.
# We have provided an example json output here for you to look at,
# but you will not be able to run any queries through our UI.
import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print("requesting", r.url)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print(json.dumps(data, indent=indent, sort_keys=True))
    else:
        print(data)


def main():
    results = query_by_name(ARTIST_URL, query_type["simple"], "Kelley James")
    artist_record = results['artists'][0]
    print("\nThis is the artist record")
    pretty_print(artist_record)


    index=0
    artist_id = results["artists"][index]["id"]
    artist_name = results["artists"][index]["name"]
    artist_dis = results["artists"][index].get('disambiguation',"")
    artist_home = results["artists"][index].get("begin-area",False)
    if artist_home:
        artist_home = artist_home["name"]

    print("\nARTIST:")
    print("    name: %s - %s" % (artist_name,artist_dis))
    print("    from: %s" % artist_home)
    print("    id:   %s" % artist_id)


    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    print('\nArtist releases')
    pretty_print(artist_data)

    releases = artist_data["releases"]

    if not releases:
        print('\nNo Releases Found!')
    else:

        titles=[]
        latestdate = '1900-01-01'
        latesttitle = ""
        for r in releases:
            # each remease can be released multiple times, we care about the first time
            event_date="2015-12-31"
            for re in r['release-events']:
                if re['date'] < event_date:
                    event_date = re['date'] # find first release date
            if r['title'] not in titles:
                titles.append({'title': r['title'], 'date': event_date})

        print("\nALL TITLES:")

        for t in titles:
            print("    %s (%s)" % (t['title'], t['date']))


if __name__ == '__main__':
    main()

