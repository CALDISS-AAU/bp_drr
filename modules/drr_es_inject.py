from elasticsearch import Elasticsearch 
import time

fields = {"id": {"type": "keyword"},
          "url": {"type": "keyword", "fields":{"flex": {"type": "text", "analyzer": "english"}}},
          "domain_url": {"type": "keyword"},
          "text": {"type": "text", "analyzer": "english"},
          "org": {"type": "keyword"},
          "page_links": {"type": "keyword", "fields":{"flex": {"type": "text", "analyzer": "english"}}},
          "type": {"type": "keyword"}
		  }
		  
		  
def connect(passwd, user = 'elastic', host='localhost', port=9200):
    return Elasticsearch([{'host':host,'port':port}], http_auth=(user, passwd))


def create(es, delete=True, index='drr'):
    mappings = {
        "mappings":{
            "properties": fields
        }
    }
    
    if delete:
        try:
            rd = es.indices.delete(index=index)
        except:
            print('Could not delete index {}'.format(index))

    es.indices.create(index=index, body=mappings)

def verify_docs(docs, verbose=False):
    """
    Iterate through all docs, and verify if any fields/keys are missing or of the wrong type

    """

    for docno, doc in docs.items():
        for key in fields.keys():
            if key not in doc:
                if verbose:
                    print('Missing key/field {} in index {}'.format(key, docno))
                return False

    return True

def inject_doc(es, docno, doc, index='drr', verbose=False):
    
    es.index(index=index, doc_type='_doc', id=docno, body=doc)

def inject(docs, index='drr', host='localhost', port=9200, verbose=False, verify=True):

    if verify:
        if verify_docs(docs, verbose=verbose):
            pass
        else:
            return None
        
    docnos = []
    es = connect(host, port)
    create(es, index=index)
    
    for key in docs:
        doc = docs[key]
        docno = doc['id']

        if verify == False:  # add empty keys
            for key in fields.keys():
                if key not in doc:
                    doc[key] = ''

        inject_doc(es, docno, {k:doc[k] for k in fields}, index = index, verbose=verbose) # only take the fields thats described
        docnos.append(docno)
        
    return docnos