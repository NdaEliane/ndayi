from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=2MkWkqk8uts').streams.first().download()
yt = YouTube('https://www.youtube.com/watch?v=2MkWkqk8uts')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()