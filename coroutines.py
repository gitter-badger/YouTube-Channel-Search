# Import Tornado Libraries
from tornado.httpclient import AsyncHTTPClient
from tornado import gen, escape


# coroutines.py has all the coroutines (async calls), for our handlers

@gen.coroutine
def fetch_coroutine(url):
    # Usage:
    #       This is a fetch URL coroutine, it will get the response of a rest api
    #       which will be in a json format, and this will be passed back as an end result
    # Arguments:
    #       url: a single url, for example, http://youtubeapi.com/setting?a=1
    # Return:
    #       json object: the json object that is returned by a rest api

    # Create an AsyncHTTPClient for asynchrounous calls
    http_client = AsyncHTTPClient()

    # Yield the fetch of http_client so that the ioloop can do other things
    response = yield http_client.fetch(url)

    # Returns a json file decoded
    raise gen.Return(escape.json_decode(response.body))

@gen.coroutine
def parallel_fetch_coroutine(urls):
    # Usage:
    #       This is a fetch URL coroutine, it will get the response of a rest api
    #       which will be in a json format, and this will be passed back as an end result.
    #       It is almost the same as fetch_coroutine function, but takes in an array of urls
    #       so that we can fetch multiple json files in parallel.
    # Arguments:
    #       url: a list of urls, for example
    #            ['http://youtubeapi.com/setting?a=1', 'http://youtubeapi.com/setting?a=2']
    # Return:
    #       a list of json object: It will return a list of json object
    #                              for example: ['json1', 'json2'] where json1 corresponds to the
    #                                           json file from 'http://youtubeapi.com/setting?a=1'

    # Create an Async http client
    http_client = AsyncHTTPClient()

    # Yield multiple urls in parallel
    responses = yield [http_client.fetch(url) for url in urls]

    # Return a list of json objects
    raise gen.Return([escape.json_decode(response.body) for response in responses])