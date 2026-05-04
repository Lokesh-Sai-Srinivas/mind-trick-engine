# 🧠 Jedi Mind Trick Engine

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-green.svg)
![DeepFace](https://img.shields.io/badge/DeepFace-Facial_Analysis-orange.svg)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-OS_Control-red.svg)

An interactive, AI-powered Desktop Interface that lets you control your operating system using only your facial expressions—like a Jedi Mind Trick. 

This engine uses your webcam to run real-time facial emotion recognition, translating your expressions directly into hardware-level keyboard and mouse commands.

---

## ✨ Features

- **Real-Time Facial Analysis**: Analyzes video frames on-the-fly to detect dominant emotions.
- **Hands-Free OS Control**:
  - 😄 **Happy (Smile)** = Press `Space` (Play/Pause media).
  - 😠 **Angry (Scowl)** = Scroll **Down** the active window.
  - 😲 **Surprise (Raised Eyebrows)** = Scroll **Up** the active window.
- **Optimized for Performance**: Includes a frame-skipping mechanism so DeepFace doesn't bottleneck your CPU/GPU.
- **Smart Cooldowns**: Built-in timers prevent input-spamming, ensuring a smooth scrolling and media playback experience.
- **Live HUD Overlay**: Displays exactly what the AI is seeing and tracks cooldown status natively on the video feed.
- **Emergency Failsafes**: Built-in PyAutoGUI failsafes to instantly crash the script and return control if the AI goes rogue.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **OpenCV (`cv2`)**: For capturing the webcam feed, mirroring the video, and drawing the HUD overlay.
- **DeepFace**: A lightweight facial recognition and attribute analysis framework wrapping TensorFlow/Keras.
- **PyAutoGUI**: For simulating native OS hardware inputs (mouse scrolls, keyboard presses).

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/jedi-mind-trick-engine.git
   cd jedi-mind-trick-engine
   ```

2. **Create a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Core Dependencies:**
   ```bash
   pip install opencv-python pyautogui deepface
   ```

4. **Install Backend & Compatibility Packages:**
   Depending on your TensorFlow version, you will likely need the Keras legacy adapter and Windows C++ Runtimes.
   ```bash
   pip install tf-keras msvc-runtime
   ```

*(Note: The very first time you run the script, DeepFace will automatically download its pre-trained facial emotion weights, which is roughly 20-30MB).*

---

## 🎮 Usage

1. **Run the Engine:**
   ```bash
   python mind_trick_engine.py
   ```
2. **Setup your environment:**
   - Wait for the OpenCV window to open (TensorFlow may take 5-10 seconds to warm up).
   - Open a web browser (like a YouTube video or a long article) and place it side-by-side with the OpenCV window.
   - **Click inside your web browser so it becomes the Active Window.**
3. **Use the Force:**
   - Smile to pause/play the video.
   - Scowl to scroll down the page.
   - Look surprised to scroll up the page.

---

## ⚠️ Troubleshooting & Known Issues

- **DLL Load Failed / INITIALIZATION FAILED (0x45A)**
  - *Cause*: TensorFlow's C++ binaries are clashing with OpenCV, or you are missing Microsoft Visual C++ Redistributables.
  - *Fix*: Ensure `import tensorflow as tf` is the **very first line** in the script, above OpenCV. Run `pip install msvc-runtime`.
  
- **Lag or Freezing:**
  - *Fix*: Open the script and increase `FRAME_SKIP = 5` to `10` or `15`. This forces the AI to analyze fewer frames per second, significantly reducing CPU load.

- **PyAutoGUI is scrolling too little/too much:**
  - *Fix*: Modify the `SCROLL_AMOUNT = 500` variable. Windows and macOS interpret scroll ticks very differently. Drop it to `100` if it's too fast, or raise it to `1000` if it barely moves.

- **The script is spamming keys uncontrollably!**
  - *Emergency Abort*: Slam your physical mouse cursor into any of the **4 extreme corners** of your physical monitor. This triggers PyAutoGUI's built-in failsafe and instantly terminates the program.

---

## 📝 License
This project is for educational and entertainment purposes. Feel free to fork, modify, and expand the emotion triggers!
