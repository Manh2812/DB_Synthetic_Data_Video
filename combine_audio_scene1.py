from moviepy import VideoFileClip, AudioFileClip
import os

# Đường dẫn video HD (sau khi render -qh)
video_path = "output/videos/scene1_intro/1080p60/Scene1Intro.mp4"
audio_path = "assets/audio/scene1_intro.mp3"
output_path = "output/videos/scene1_intro/Scene1Intro_HD_with_audio.mp4"

# Kiểm tra file
for f in [video_path, audio_path]:
    if not os.path.exists(f):
        raise FileNotFoundError(f"Không tìm thấy: {f}")

# Ghép audio
video = VideoFileClip(video_path)
audio = AudioFileClip(audio_path)
final = video.with_audio(audio)
final.write_videofile(output_path, codec="libx264", audio_codec="aac")
print("✅ Hoàn tất:", output_path)