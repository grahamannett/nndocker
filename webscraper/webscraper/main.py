from ratelimit import RateLimiter
from relatedvids import RelatedVid
from postgresDB import db
import re

class YouTubeScraper(object):

    """
    given a youtube video url, return captions and related captions for vids
    recursively

    url: base url of youtube video to use
    level: number of levels 'deep' to go to search for vids
    n_related: number of related videos to get on each level
    level: 0, recursive level to start at

    idea is:
    1. with url, check if in postgresDB already
        1a. if video in postgresDB check level, if level is same then video has
            already been scraped, -> end
        1b. if level is different then update level to 0 and start as if video
            was never previously scraped -> 2
    2. return captions and related videos and write to postgresDB
    3.
    """

    def __init__(self, url, level=5, n_related=10):
        self.url = url
        self.videoId = self.videoId_()

    @property
    def videoId_(self):
        # could just use 'youtu' but including both for clarity
        if 'youtube.' or 'youtu.be' in self.url:
            # clean url
            return re.split('=|&', self.url)[1]
        else:
            return self.url

    def check_db_for_vid(self):
        """
        check if videoId in database
        """
        with db.cursor() as cursor:
                    if self.videoId in db.
            pass

    def return_related_vids(self):
        """
        return related vids from videoId
        """

        self.relatedVids_ = RelatedVid(self.videoId)

    def get_captions(self):
        with RateLimiter():
