from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

def merge_video_with_image(video_path, image_path, output_path):
    # Load the video and image
    video = VideoFileClip(video_path)
    image = ImageClip(image_path).set_duration(video.duration)
    
    # Create a composite video with the image as background and video on top
    final_clip = CompositeVideoClip([image, video.set_position("center")])
    
    # Write the result to a file
    final_clip.ipython_display()  

def merge_videos(video1_path, video2_path, output_path):
    # Load both videos
    video1 = VideoFileClip(video1_path)
    video2 = VideoFileClip(video2_path)
    
    # Resize videos if necessary (example: resize to half the original width)
    video1 = video1.resize(width=video1.w // 2)
    video2 = video2.resize(width=video2.w // 2)
    
    # Create a composite video with both videos side by side
    final_clip = CompositeVideoClip([video1.set_position((0, 0)),
                                     video2.set_position((video1.w, 0))])
    
    # Write the result to a file
    final_clip.ipython_display()  

# Example usage
ai_avatar_video = "video1.mkv"
image = "image.png"
other_video = "video2.mkv"

merge_video_with_image(ai_avatar_video, image, "output_with_image.mp4")
merge_videos(ai_avatar_video, other_video, "output_two_videos.mp4")
