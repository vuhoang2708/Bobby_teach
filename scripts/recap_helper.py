import os
import glob
import subprocess
import sys
import time
import shutil
import urllib.request

def find_ffmpeg():
    """
    Search for FFmpeg executable in system PATH, common ShareX locations, and local dirs.
    """
    # 1. Check system PATH
    ffmpeg_in_path = shutil.which("ffmpeg")
    if ffmpeg_in_path:
        return ffmpeg_in_path

    # 2. Check local directories relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    
    local_paths = [
        os.path.join(script_dir, "ffmpeg.exe"),
        os.path.join(repo_root, "ffmpeg.exe"),
        os.path.join(repo_root, "tools", "ShareX", "ffmpeg.exe"),
    ]
    for lp in local_paths:
        if os.path.exists(lp):
            return lp

    # 3. Check common ShareX Windows directories
    local_app_data = os.environ.get("LOCALAPPDATA", "")
    program_files = os.environ.get("ProgramFiles", "")
    program_files_x86 = os.environ.get("ProgramFiles(x86)", "")

    sharex_paths = []
    if local_app_data:
        sharex_paths.append(os.path.join(local_app_data, "ShareX", "ffmpeg.exe"))
    if program_files:
        sharex_paths.append(os.path.join(program_files, "ShareX", "ffmpeg.exe"))
    if program_files_x86:
        sharex_paths.append(os.path.join(program_files_x86, "ShareX", "ffmpeg.exe"))

    for sp in sharex_paths:
        if os.path.exists(sp):
            return sp

    return None

def download_ffmpeg(target_dir):
    """
    Downloads portable FFmpeg if missing.
    """
    os.makedirs(target_dir, exist_ok=True)
    ffmpeg_path = os.path.join(target_dir, "ffmpeg.exe")
    
    # Official ShareX FFmpeg release download link (portable, compact build)
    url = "https://github.com/ShareX/FFmpeg/releases/download/v7.0.1/ffmpeg.exe"
    
    print("\n[FFmpeg Not Found] FFmpeg is required for audio extraction.")
    print(f"Downloading FFmpeg from: {url}")
    print("This will take a moment, please wait...")

    try:
        def progress_callback(block_num, block_size, total_size):
            read_so_far = block_num * block_size
            if total_size > 0:
                percent = min(100, int(read_so_far * 100 / total_size))
                sys.stdout.write(f"\rDownloading: {percent}% ({read_so_far // (1024*1024)}MB / {total_size // (1024*1024)}MB)")
                sys.stdout.flush()
            else:
                sys.stdout.write(f"\rDownloading: {read_so_far // (1024*1024)}MB")
                sys.stdout.flush()

        urllib.request.urlretrieve(url, ffmpeg_path, progress_callback)
        print("\nDownload complete! FFmpeg is now ready.")
        return ffmpeg_path
    except Exception as e:
        print(f"\nError downloading FFmpeg: {e}")
        print("Please download ffmpeg.exe manually and place it in the 'scripts' folder.")
        return None

def find_latest_video():
    """
    Locates the most recent video file in ShareX screenshots folders.
    """
    # Build list of potential ShareX screenshot locations
    user_documents = os.path.expanduser(r"~\Documents")
    local_app_data = os.environ.get("LOCALAPPDATA", "")
    
    search_dirs = []
    if user_documents:
        search_dirs.append(os.path.join(user_documents, "ShareX", "Screenshots"))
    if local_app_data:
        search_dirs.append(os.path.join(local_app_data, "ShareX", "Screenshots"))
        
    # Also search relative to this repository
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    search_dirs.append(os.path.join(repo_root, "tools", "ShareX", "ShareX", "Screenshots"))

    video_extensions = ['*.mp4', '*.mkv', '*.avi', '*.webm']
    latest_file = None
    latest_time = 0

    print("Scanning directories for screen recordings:")
    for base_dir in search_dirs:
        if not os.path.exists(base_dir):
            continue
        print(f" - Scanning: {base_dir}")
        for ext in video_extensions:
            files = glob.glob(os.path.join(base_dir, '**', ext), recursive=True)
            for f in files:
                try:
                    mtime = os.path.getmtime(f)
                    if mtime > latest_time:
                        latest_time = mtime
                        latest_file = f
                except Exception:
                    pass
                    
    return latest_file

def main():
    # Force UTF-8 stdout encoding for safety in Windows Console environments
    if hasattr(sys.stdout, 'reconfigure'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    
    # Destination folder for recaps in the repo
    output_dir = os.path.join(repo_root, "recaps")
    
    print("="*60)
    print("BOBBY CLASS RECAP AUTOMATION TOOL")
    print("="*60)

    # 1. Find or Download FFmpeg
    ffmpeg_path = find_ffmpeg()
    if not ffmpeg_path:
        # Download FFmpeg directly into scripts folder
        ffmpeg_path = download_ffmpeg(script_dir)
        if not ffmpeg_path:
            sys.exit(1)
    else:
        print(f"FFmpeg found at: {ffmpeg_path}")

    # 2. Find Latest Video
    latest_video = find_latest_video()
    if not latest_video:
        print("\n[!] No video recordings found in ShareX Screenshot directories.")
        print("Please verify that:")
        print("1. ShareX is installed and has been used to record a video.")
        print("2. The video is saved under documents/ShareX/Screenshots.")
        sys.exit(1)

    print(f"\n[+] Latest recording detected: {latest_video}")
    
    # 3. Perform Extraction
    os.makedirs(output_dir, exist_ok=True)
    video_basename = os.path.basename(latest_video)
    video_name, _ = os.path.splitext(video_basename)
    output_audio_path = os.path.join(output_dir, f"{video_name}_audio.mp3")

    print(f"-> Extracting audio to: {output_audio_path}")
    
    cmd = [
        ffmpeg_path,
        '-y',
        '-i', latest_video,
        '-vn',
        '-acodec', 'libmp3lame',
        '-q:a', '2',
        output_audio_path
    ]

    try:
        start_time = time.time()
        # Hide output windows on Windows to keep CLI clean
        startupinfo = None
        if os.name == 'nt':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, startupinfo=startupinfo)
        elapsed = time.time() - start_time
        print(f"Success! Audio extracted in {elapsed:.2f} seconds.")
        print(f"\nReady for upload! Copy this path to upload to NotebookLM/Gemini:")
        print(f"Path: {output_audio_path}")
    except subprocess.CalledProcessError as e:
        print("FFmpeg extraction failed:")
        print(e.stderr.decode('utf-8', errors='ignore'))
        sys.exit(1)

if __name__ == "__main__":
    main()
