import datetime
import logging
import time


def convertTimeToUnixTimestamp(time):
    return (time - datetime.datetime(1970, 1, 1)).total_seconds()


def getCurrentTime():
    return convertTimeToUnixTimestamp(datetime.datetime.now())


class RateLimiter():
    rate = 2.0  # unit: actions (float)
    per = 1.0  # unit: seconds (float)
    allowance = rate  # unit: actions (float)
    lastCheck = getCurrentTime()  # unit: seconds

    @staticmethod
    def waitForRateLimit():
        """
        blocks until it is okay to proceed
        """
        while not RateLimiter.rateLimiter():
            logging.debug("being rate limited")
            time.sleep(0.5)

    @staticmethod
    def rateLimiter():
        current = getCurrentTime()
        time_passed = current - RateLimiter.lastCheck
        RateLimiter.lastCheck = current
        RateLimiter.allowance += time_passed * \
            (RateLimiter.rate / RateLimiter.per)
        if (RateLimiter.allowance > RateLimiter.rate):
            logging.debug(
                "throttling, {}, {}".format(
                    RateLimiter.allowance, RateLimiter.rate))
            RateLimiter.allowance = RateLimiter.rate  # throttle
        if (RateLimiter.allowance < 1.0):
            logging.debug("returning false, {}, {}".format(
                RateLimiter.allowance, RateLimiter.rate))
            return False
        else:
            logging.debug("returning true, {}, {}".format(
                RateLimiter.allowance, RateLimiter.rate))
            RateLimiter.allowance -= 1.0
            return True
