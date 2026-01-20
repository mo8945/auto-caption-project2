import os
import subprocess

# 프로그램 실행 전, 파이썬이 ffmpeg 위치를 알 수 있게 일시적으로 경로를 추가합니다.
ffmpeg_path = r"C:\ffmpeg\bin"
os.environ["PATH"] += os.pathsep + ffmpeg_path

# 테스트: 이제 에러 없이 버전이 출력되는지 확인
try:
    subprocess.run(["ffmpeg", "-version"], check=True)
    print("✅ ffmpeg 연결 성공!")
except FileNotFoundError:
    print("❌ 여전히 경로를 찾을 수 없습니다. 폴더명을 다시 확인하세요.")