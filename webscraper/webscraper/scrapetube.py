from pydub import AudioSegment
from os.path import isfile
import speech_recognition as sr
import os
import pafy
import youtube_dl
import urllib
import pysrt


class youtube_video(object):

    """
    for url return captions and related vids for that url
    """

    def __init__(self, url, n_related=10):
        pass


class youtube_source(object):

    """
    youtube_source

    Args:
        url: url of video online

    Attributes:

    +++++
    todo:
    - plan on incorporating audio snippets in db of some type since there is no
    - seperate out save and load wav files
    +++++
    important libraries:

    audio library:
    https://github.com/jiaaro/pydub

    google speech recognition library:
    https://github.com/Uberi/speech_recognition

    downloading audio from youtube:
    http://pythonhosted.org/pafy/
    """

    def __init__(self, url):
        """
        ill explain this later i guess
        """
        self.url = url
        self.test
        if querydbforvideo(self.url):
            # subtitle already downloaded, dont download or use youtube-dl
            self.text = pysrt.open
        else:

            self.ydl_opts = {'no_warnings': True,
                             'quiet': True,
                             'simulate': True,
                             'subtitles': 'en',
                             'verbose': False}

            self.subtitlesavailable = self.are_subs_available()

            # if AutoSubs is True, dont need to use Google API
            if self.subtitlesavailable:
                self.grab_auto_subs()
                # download subtitles and then move on
            else:
                # download other way
                if 'youtube' in url:
                    self.audio = pafy.new(url).getbestaudio(preftype="m4a")

                    # if files already downloaded, dont download again
                    if isfile('youtube/audio/' + self.title):
                        self.savedlocation = 'youtube/audio/' + \
                            self.audio.generate_filename()
                        print('file already downloaded \n')
                    else:
                        self.savedlocation = self.download_as_audio()
            # self.savedlocation = self.download_as_audio()

    def __str__(self):

        return self.title

    def text_from_srt(self, location):

        text = pysrt.open('youtube/dl-texts/' + self.title + '.srt')

        return text.text.replace('\n', ' ')

    def are_subs_available(self):
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            subs = ydl.extract_info(self.url, download=False)
        if os.path.isfile('youtube/dl-texts' + subs['title'] + '.srt'):
            return text_from_srt('youtube/dl-texts' + subs['title'] + '.srt')
        elif subs['requested_subtitles']:
            self.title = subs['title']
            self.subs_url = subs['requested_subtitles']['en']['url']
            return True
        else:
            return False

    def parse_youtube_url(self):
        if 'youtube.com' in self.url:
            self.videoId = self.url.split('=')[1]
        else:
            self.videoId = self.url

    def grab_auto_subs(self):
        """
        """
        try:
            urllib.request.urlretrieve(
                self.subs_url, 'youtube/dl-texts/' + self.title + '.srt')
            print("subtitles saved directly from youtube\n")
            text = pysrt.open('youtube/dl-texts/' + self.title + '.srt')
            self.text = text.text.replace('\n', ' ')
        except IOError:
            print("\n *** saving sub's didn't work *** \n")

        # if youtube_dl(self.url).ClosedCaptionsOrSubtitlesAvailable:
        # if the subtitles or closed captions are available, dont do google
        # speech stuff
        #     options = [
        #         'dont download', 'get cc', 'get
        # subtitles', 'youtube-dl-texts']
        #     youtube_dl(url, options)
        # return True

    def convert_cc_subs_to_textfile(self):
        """
        if youtube-dl has subtitles or closed captions, use that one module to
        convert to single text file since otherwise you will get time and
        whatever
        """

    def download_as_audio(self):
        # audio = pafy_
        if 'youtube' in self.audio.url:

            self.audio.download(
                filepath='audio-youtube/' + self.audio.filename, quiet=False)

        return 'audio-youtube/' + self.audio.filename

    def remove_silence(self):
        # do this later, theres a method in pydub but it doesn't seem to work
        # on all
        pass

    def trim_audio(self, timestart, timestop, remove_silence=False):
        """
        trim the audio from
        [timestart:timestop]
        timestamps are strings
        since a lot of the vids have nothing useful or sound...

        going for ~5 second phrases at this point
        """

        self.timestart = timestart
        self.timestop = timestop
        # convert time to seconds since that's what pydub wants
        ftr = [60, 1]
        timestart = sum(
            [a * b for a, b in zip(ftr, map(int, timestart.split(':')))])
        timestop = sum(
            [a * b for a, b in zip(ftr, map(int, timestop.split(':')))])

        audio = AudioSegment.from_file(self.savedlocation)

        # pydub uses milliseconds so multiply seconds for correct slice
        audio = audio[(timestart * 1000):(timestop * 1000)]

        if remove_silence:
            # the default settings didnt work at all...
            # this seems better but would need to fix later
            print('current length: {0}'.format(audio.duration_seconds))

            audio = audio.strip_silence(
                silence_len=250, silence_thresh=-35, padding=10.0)

            print('length with strip_silence: {0}'.format(
                audio.duration_seconds))

        # set to mono so it will work with speech recognizer thing
        audio = audio.set_channels(1)

        audio.export(
            out_f='audio-trimmed/' + self.audio.title + self.timestart +
            '-' + self.timestop + '.wav', format='wav')
        self.trimmed_location = 'audio-trimmed/' + \
            self.audio.title + self.timestart + '-' + self.timestop + '.wav'

    def convert_audio_to_text_(self, personal_key=True):
        """
        convert audio from .wav format to text

        Set personal_key = True to use your own personal key otherwise you are
        using

        BELOW IS WRONG.  SEEMS TO WORK NOW BUT KEEPING IN CASE
        example doesnt work for some reason...
        what i need to do (or edit the library to do) for example is:

        EX:

        >>> wav_file = sr.WavFile('test.wav')
        >>> wav_file.__enter__()

        >>> audio = recognizer.record(wav_file)
        >>> recognizer.recognize(audio)


        test
        """
        if personal_key:
            key = open('credentials')
            key = key.read().split('=')[1]
            recognizer = sr.Recognizer(key=key)
            print('using personal_key')

        else:

            recognizer = sr.Recognizer()
            print('using key from speech_recognition')
        # pass it the trimmed location file
        with sr.WavFile(self.trimmed_location) as source:
            audio = recognizer.record(source)

        # save all possible texts but just return the first/most possible one
        self.texts = recognizer.recognize(audio, True)
        return self.texts[0]["text"]
        # self.text = recognizer.recognize(audio)
        # return self.speech_to_text_ = recognizer.recognize(audio, True)

    def write_text_to_file_(self):
        # write text to csv in folder (plan to use some database in future)
        text_file = open(
            "texts/" + self.audio.filename.split('.')[:-1][0] +
            self.timestart + '-' + self.timestop + ".csv", "w")

        # column headers
        text_file.write('confidence,text\n')
        for text in self.texts:
            # write each item in the predictions as:
            # confidence,text
            text_file.write(
                str(text['confidence']) + ',' + text['text'] + '\n')
        print("text file: texts/" + self.audio.filename.split('.')
              [:-1][0] + self.timestart + '-' + self.timestop +
              ".txt was written")


def querydbforvideo(url):
    pass
