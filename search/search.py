import elasticsearch
from elasticsearch_dsl import Search


ELASTIC_HOST = 'http://localhost:9231/'

client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST])


def lookup(query, index='products', fields=['title', 'description']):
    if not query:
        return 
    results = Search(
        index=index).using(client).query("multi_match", fields=fields, fuzziness='AUTO', query=query)

    q_results = []

    for hit in results:
        print(hit.id)
        print(hit.title)
        print(hit.description)
        print(hit.url)

        data = {
            "id": hit.id,
            "title": hit.title,
            "description": hit.description,
            "url": hit.url,
        }
        q_results.append(data)
    return q_results