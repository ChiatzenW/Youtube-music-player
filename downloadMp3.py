import pytube, os
from moviepy.audio.io.AudioFileClip import AudioFileClip

def main(name):
    if not os.path.exists('tmp'):
                os.mkdir('tmp')

    #search for a video
    srch = name
    s = pytube.Search(srch)
    yt=s.results[0]

    #download audio-only mp4 with the highest abr
    yt.streams.filter(type='audio')
    highest_strm=yt.streams.get_audio_only()
    mp4_filename=highest_strm.download(output_path='tmp')

    # write to mp3 and remove mp4
    audio_file = AudioFileClip(mp4_filename)
    audio_file.write_audiofile(mp4_filename[:-4] + ".mp3")
    audio_file.close()
    os.remove(mp4_filename)

if __name__ == "__main__":
   main()