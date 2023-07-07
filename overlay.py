from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import AudioFileClip
from moviepy.editor import CompositeAudioClip
import os
from datetime import datetime


def compose_video(dir_path: str, times: list) -> None:
    title_audio = AudioFileClip(f'{dir_path}/title.mpeg')
    audio = AudioFileClip(f'{dir_path}/text.mpeg').set_start(title_audio.duration + 1)

    final_audio = CompositeAudioClip([title_audio, audio])

    video = VideoFileClip('/tmp/minecraft15.mp4').subclip(0, final_audio.duration + 1)
    video = video.set_audio(final_audio)

    title_img_file = f"{dir_path}/img_title.png"
    title_img = ImageClip(title_img_file) \
        .set_duration(title_audio.duration) \
        .set_start(0) \
        .set_position('center', 'center')
    os.remove(title_img_file)

    clips = [video, title_img]

    for i in range(len(times)):
        start = times[i][0]
        duration = times[i][1] - start
        img_file = f"{dir_path}/img_{i}.png"
        img_clip = ImageClip(img_file) \
            .set_duration(duration) \
            .set_start(title_audio.duration + 1 + start) \
            .set_position('center', 'center')
        clips.append(img_clip)
        os.remove(img_file)

    final = CompositeVideoClip(clips)

    final.write_videofile(f'{dir_path}/output.mp4', codec='mpeg4', audio_codec='aac', fps=60)
