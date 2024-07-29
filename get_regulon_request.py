import json
import requests
import time
url = "https://regulondb.ccg.unam.mx/graphql"
body= """
query GetRegulonBy($advancedSearch: String, $search: String) {
  getRegulonBy(advancedSearch: $advancedSearch, search: $search) {
    data {
      _id
      aligmentMatrix {
        aligment
        consensus
        matrix
        urlMatrixQualityResult
        urlPWMLogo
        __typename
      }
      allCitations {
        evidence {
          _id
          additiveEvidenceCodeRule
          code
          name
          type
          __typename
        }
        publication {
          _id
          authors
          citation
          pmid
          title
          url
          year
          __typename
        }
        __typename
      }
      evolutionaryConservation {
        urlPromoterTargetGene
        urlRegulatorTargetGene
        __typename
      }
      organism {
        _id
        name
        __typename
      }
      regulates {
        genes {
          _id
          function
          name
          terms {
            geneOntology {
              biologicalProcess {
                _id
                name
                __typename
              }
              cellularComponent {
                _id
                name
                __typename
              }
              molecularFunction {
                _id
                name
                __typename
              }
              __typename
            }
            multifun {
              _id
              genes {
                _id
                name
                __typename
              }
              name
              __typename
            }
            __typename
          }
          __typename
        }
        operons {
          _id
          firstGene {
            _id
            name
            __typename
          }
          function
          name
          __typename
        }
        sigmaFactors {
          _id
          function
          gene {
            _id
            name
            __typename
          }
          name
          __typename
        }
        transcriptionFactors {
          _id
          function
          name
          __typename
        }
        transcriptionUnits {
          _id
          function
          name
          promoter {
            _id
            name
            __typename
          }
          firstGene {
            _id
            name
            __typename
          }
          __typename
        }
        __typename
      }
      regulator {
        _id
        abbreviatedName
        additiveEvidences {
          category
          code
          type
          __typename
        }
        citations {
          evidence {
            _id
            additiveEvidenceCodeRule
            code
            name
            type
            __typename
          }
          publication {
            _id
            authors
            citation
            pmid
            title
            url
            year
            __typename
          }
          __typename
        }
        confidenceLevel
        conformations {
          _id
          class
          confidenceLevel
          effector {
            _id
            name
            __typename
          }
          effectorInteractionType
          functionalType
          name
          note
          type
          __typename
        }
        connectivityClass
        encodedBy {
          genes {
            _id
            leftEndPosition
            length
            name
            rightEndPosition
            __typename
          }
          operon {
            _id
            name
            tusEncodingRegulator {
              promoterName
              transcriptionUnitName
              __typename
            }
            __typename
          }
          __typename
        }
        family
        function
        name
        note
        products {
          _id
          abbreviatedName
          name
          __typename
        }
        sensingClass
        siteLength
        symmetry
        synonyms
        type
        __typename
      }
      regulatoryInteractions {
        _id
        activeConformation {
          _id
          name
          type
          __typename
        }
        additiveEvidences {
          category
          code
          type
          __typename
        }
        citations {
          evidence {
            _id
            additiveEvidenceCodeRule
            code
            name
            type
            __typename
          }
          publication {
            _id
            authors
            citation
            pmid
            title
            url
            year
            __typename
          }
          __typename
        }
        confidenceLevel
        distanceToFirstGene
        distanceToPromoter
        function
        regulatedEntity {
          _id
          name
          type
          __typename
        }
        regulatedGenes {
          _id
          name
          __typename
        }
        regulatoryBindingSites {
          absolutePosition
          function
          leftEndPosition
          rightEndPosition
          sequence
          strand
          __typename
        }
        __typename
      }
      summary {
        bindingSites {
          activated
          dual
          repressed
          total
          unknown
          __typename
        }
        genes {
          activated
          dual
          repressed
          total
          unknown
          __typename
        }
        operons {
          activated
          dual
          repressed
          total
          unknown
          __typename
        }
        regulatoryInteractions {
          activated
          dual
          repressed
          total
          unknown
          __typename
        }
        sigmaFactors {
          activated
          dual
          repressed
          total
          unknown
          __typename
        }
        transcriptionFactors {
          activated
          dual
          repressed
          total
          unknown
          __typename
        }
        transcriptionUnits {
          activated
          dual
          repressed
          total
          unknown
          __typename
        }
        __typename
      }
      terms {
        geneOntology {
          biologicalProcess {
            _id
            name
            __typename
          }
          cellularComponent {
            _id
            name
            __typename
          }
          molecularFunction {
            _id
            name
            __typename
          }
          __typename
        }
        multifun {
          _id
          genes {
            _id
            name
            __typename
          }
          name
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
}"""
def get_regulon_data(regulon_id):
    request = {"operationName" : "GetRegulonBy", "query": body, "variables": {"advancedSearch": regulon_id + "[_id]"}}
    while True:
        try:
            response = json.loads(requests.post(url = url, json = request, verify = False).content)
            time.sleep(1)
            break
        except:
            time.sleep(1)
            continue
    return response

def get_triplet_description(subjekt, _id):
    triplets = []
    url = "https://regulondb.ccg.unam.mx/graphql"
    response = get_regulon_data(_id)
    for _object in response["data"]["getRegulonBy"]["data"][0]["regulates"]["genes"]:
        triplets.append({"subjekt" : subjekt, "predikat" : _object["function"], "objekt" : _object["name"]})
    return triplets
