import pymongo

class DataHandler:
    def __init__(self):
        self.DB_NAME = 'guesty'
        self.COLLECTION = 'data'
        self.client = pymongo.MongoClient()
        self.db = self.client[self.DB_NAME]
        self.coll = self.db[self.COLLECTION]
        self.BIAS = 0
        self.SENTIMENT_WEIGHT = 1
        self.KEYWORDS_WEIGHT = 1
        self.TIME_WEIGHT = 1
        self.GENERAL_SCORE = 1


    def read_and_analyze(self):
        for doc in self.coll.find():
            doc['sentiment_score'] = self.sentiment_analysis(doc)
            doc['keywords_score'] = self.keywords_analysis(doc)
            doc['general_score'] = self.general_parameter_analysis(doc)
            doc['timed_score'] = self.timed_analyis(doc)
            doc['grade'] = doc['sentiment_score'] * self.SENTIMENT_WEIGHT + doc['keywords_score'] * self.KEYWORDS_WEIGHT \
                        + doc['general_score'] * self.GENERAL_SCORE + doc['timed_score'] * self.TIME_WEIGHT + self.BIAS
            self.coll.save(doc)

    def get_most_urgent_messages(self,limit=10):
        result = self.coll.find().limit(limit).sort("grade",pymongo.DESCENDING)
        for doc in result:
            print(doc['grade'])
            print(doc['message'])

    def sentiment_analysis(self, doc):
        return 1

    def keywords_analysis(self, doc):
        keywords = ['asap', 'urgent', 'as soon as possible', 'acute', 'burning', 'clamant', 'compelling', 'critical', 'crying', 'dire', 'emergent', 'exigent', 'imperative', 'imperious', 'importunate', 'instant', 'necessitous', 'pressing']
        for keyword in keywords:
            if keyword in doc['message'].lower():
                return 1;
        return 0;

    def general_parameter_analysis(self, doc):
        doc['number_of_guests'] / 15 + doc['price_of_reservation'] /1000

    def timed_analyis(self, doc):
        return 1

if __name__ == "__main__":
    handler = DataHandler()
    handler.read_and_analyze()
    handler.get_most_urgent_messages()


