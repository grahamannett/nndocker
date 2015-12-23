

class wordset(object):

    """
    maxlen
    """

    def __init__(self, text):
        self.text = text
        self.maxlen = 5
        self.step = 1
        pass

    def get_text(self):
        """get text from postgres
        """
        words = set(self.text.split(' '))
        pass
