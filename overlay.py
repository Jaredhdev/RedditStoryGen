from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip


def compose_video(video_path: str, images_folder: str, times: list, out_path: str) -> None:
    video = VideoFileClip(video_path)
    clips = [video]

    for i in range(len(times)):
        img_clip = ImageClip(f"{images_folder}/img_{i}.png").set_duration(1).set_start(i).set_position('center',
                                                                                                       'center')
        clips.append(img_clip)

    final = CompositeVideoClip(clips)
    final.write_videofile(out_path)
