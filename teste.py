from moviepy.editor import VideoFileClip

video = VideoFileClip("input.mp4")
print(hasattr(video, "subclip"))
