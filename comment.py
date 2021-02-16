class Comment():

    def __init__(self, title:str, id:str, url:str, text:str, score:int, author:str):
        self.title = title
        self.id = id
        self.url = url
        self.text = text
        self.score = score
        self.author = author

    def getTitle(self):
        return self.title

    def getId(self):
        return self.id

    def getUrl(self):
        return self.url

    def getText(self):
        return self.text

    def getScore(self):
        return self.score
        
    def getAuthor(self):
        return self.author
