from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import AudioFileClip
from datetime import datetime


def compose_video(video_path: str, audio_path: str, images_folder: str, times: list, out_folder: str) -> None:
    audio = AudioFileClip(audio_path)
    video = VideoFileClip(video_path).subclip(0, audio.duration + 1)
    video = video.set_audio(audio)

    clips = [video]

    for i in range(len(times)):
        start = times[i][0]
        duration = times[i][1] - start
        img_clip = ImageClip(f"{images_folder}/img_{i}.png") \
            .set_duration(duration) \
            .set_start(start) \
            .set_position('center', 'center')
        clips.append(img_clip)

    final = CompositeVideoClip(clips)

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    final.write_videofile(f'{out_folder}/out_{timestamp}.mp4')
