# To experiment with this code freely you will have to run this code locally.
# We have provided an example json output here for you to look at,
# but you will not be able to run any queries through our UI.
import json

import musicbrainzngs

def pprint(data, indent=4):
    if type(data) == dict:
        print(json.dumps(data, indent=indent, sort_keys=True))
    else:
        if isinstance(data,list):
            for x in data:
                pprint(x)
        else:
            print(data)

artist_id = "274add72-8e59-49c9-8de0-ac2e9ab0942e" # Kelley James
artist_id = "49576e42-fbbd-4d73-968d-93c8dcf7f065" # Plain White T's


try:
    musicbrainzngs.set_useragent('NewReleaseNotifier', 0.01, contact='dane@dacxl.com')
except:
    print('Could not set useragent')

# try:
#     x=musicbrainzngs.search_artists(query='Plain White')
# except:
#     print('Search failed')

# pprint(x['artist-list'])

try:
    result = musicbrainzngs.get_artist_by_id(artist_id)
except musicbrainzngs.WebServiceError as exc:
    print("Something went wrong with the request: %s" % exc)
else:
    artist = result["artist"]
    print("name:\t\t%s" % artist["name"])
    print("sort name:\t%s" % artist["sort-name"])

result = musicbrainzngs.get_artist_by_id(artist_id,
              includes=["release-groups"], release_type=["album", "ep"])
for release_group in result["artist"]["release-group-list"]:
    print("{title} ({type})".format(title=release_group["title"],
                                    type=release_group["type"]))
    pprint(release_group)





# BASE_URL = "http://musicbrainz.org/ws/2/"
# ARTIST_URL = BASE_URL + "artist/"

# query_type = {  "simple": {},
#                 "atr": {"inc": "aliases+tags+ratings"},
#                 "aliases": {"inc": "aliases"},
#                 "releases": {"inc": "releases"}}


# def query_site(url, params, uid="", fmt="json"):
#     params["fmt"] = fmt
#     r = requests.get(url + uid, params=params)
#     print("requesting", r.url)

#     if r.status_code == requests.codes.ok:
#         return r.json()
#     else:
#         r.raise_for_status()


# def query_by_name(url, params, name):
#     params["query"] = "artist:" + name
#     return query_site(url, params)





# def main():
#     results = query_by_name(ARTIST_URL, query_type["simple"], "Kelley James")
#     artist_record = results['artists'][0]
#     print("\nThis is the artist record")
#     pretty_print(artist_record)


#     index=0
#     artist_id = results["artists"][index]["id"]
#     artist_name = results["artists"][index]["name"]
#     artist_dis = results["artists"][index].get('disambiguation',"")
#     artist_home = results["artists"][index].get("begin-area",False)
#     if artist_home:
#         artist_home = artist_home["name"]

#     print("\nARTIST:")
#     print("    name: %s - %s" % (artist_name,artist_dis))
#     print("    from: %s" % artist_home)
#     print("    id:   %s" % artist_id)


#     artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
#     print('\nArtist releases')
#     pretty_print(artist_data)

#     releases = artist_data["releases"]

#     if not releases:
#         print('\nNo Releases Found!')
#     else:

#         titles=[]
#         latestdate = '1900-01-01'
#         latesttitle = ""
#         for r in releases:
#             # each remease can be released multiple times, we care about the first time
#             event_date="2015-12-31"
#             for re in r['release-events']:
#                 if re['date'] < event_date:
#                     event_date = re['date'] # find first release date
#             if r['title'] not in titles:
#                 titles.append({'title': r['title'], 'date': event_date})

#         print("\nALL TITLES:")

#         for t in titles:
#             print("    %s (%s)" % (t['title'], t['date']))


# if __name__ == '__main__':
#     main()

