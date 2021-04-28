
#Head

import datetime
import csv

#Defs

from googleapiclient.discovery import build

api_key = #redacted

startSearch = datetime.datetime.utcnow() - datetime.timedelta(days=300)
endSearch = datetime.datetime.utcnow() - datetime.timedelta(days=299)

for x in range(0, 2):

    request = youtube.search().list(
        part = 'snippet',
        order = 'viewCount',
        publishedBefore = endSearch.isoformat("T") + "Z",
        publishedAfter = startSearch.isoformat("T") + "Z",
        relevanceLanguage = 'en',
        type = 'video',
        q = 'learn+part',
        videoDuration = 'long', #By actual courses, so long videos (over 20 minutes)
        maxResults = 50,
    )

    startSearch = startSearch + datetime.timedelta(days=1)
    endSearch = endSearch + datetime.timedelta(days=1)
    response = request.execute()
    results = storeResults(response)
    print(response)
"""
"""
request = youtube.search().list(
        part = 'id,snippet',
        order = 'viewCount',
        publishedBefore = endSearch.isoformat("T") + "Z",
        publishedAfter = startSearch.isoformat("T") + "Z",
        relevanceLanguage = 'en',
        type = 'video',
        q = 'learn+part',
        videoDuration = 'long', #By actual courses, so long videos (over 20 minutes)
        maxResults = 50,
    )

response = request.execute()
results = storeResults(response)
print(results)
"""

#Run YouTube Search
q = "learn+part"
response = youtubeSearch(q)
results = storeResults(response)
#Display result titles
print("Top 3 results are: \n {0}, ({1}), \n {2}, ({3}),\n {4}, ({5})".format(results['title'][0],results['channelTitle'][0],
                                                                             results['title'][1],results['channelTitle'][1],
                                                                             results['title'][2],results['channelTitle'][2]))

#Save Results"

print("Input filename to store csv file: ")

file = input() + ".csv"

writeCSV(results, file)

print("CSV file has been uploaded at: " + str(file))
print(results)
