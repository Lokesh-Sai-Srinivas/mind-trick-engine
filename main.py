import tensorflow as tf
import cv2
from deepface import DeepFace
import pyautogui
import time

# PyAutoGUI Failsafe: Moving the mouse to any of the 4 corners of the screen will abort the program
pyautogui.FAILSAFE = True

def main():
    # Initialize webcam (0 is usually the default built-in camera)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # --- Configuration Variables ---
    FRAME_SKIP = 5          # Process 1 out of every 5 frames to save CPU/GPU resources
    COOLDOWN_TIME = 2.0     # Wait 2 seconds between triggering actions
    SCROLL_AMOUNT = 500     # Number of "clicks" to scroll up or down
    
    frame_count = 0
    last_action_time = 0.0
    current_emotion = "Neutral"

    print("========================================")
    print("      Jedi Mind Trick Engine Started    ")
    print("========================================")
    print("- Ensure your face is well-lit.")
    print("- Press 'q' in the video window to quit.")
    print("- Move mouse to any screen corner to emergency abort.")
    print("========================================")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from webcam.")
            break

        # Mirror the frame horizontally for a more natural viewing experience
        frame = cv2.flip(frame, 1)
        frame_count += 1

        # Process every Nth frame for performance optimization
        if frame_count % FRAME_SKIP == 0:
            try:
                # Analyze the frame for emotions
                # enforce_detection=False prevents crashes when no face is clearly visible
                result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                
                # DeepFace may return a list if multiple faces are found; we take the first one
                if isinstance(result, list):
                    result = result[0]
                
                # Get the dominant emotion, default to neutral if missing
                dominant_emotion = result.get('dominant_emotion', 'neutral')
                current_emotion = dominant_emotion
                
                current_time = time.time()
                
                # Check if we are past the cooldown timer
                if current_time - last_action_time > COOLDOWN_TIME:
                    
                    if current_emotion == 'happy':
                        print("Emotion: Happy -> Action: Pressing 'space' (Play/Pause)")
                        pyautogui.press('space')
                        last_action_time = current_time
                        
                    elif current_emotion == 'angry':
                        print("Emotion: Angry -> Action: Scrolling Down")
                        pyautogui.scroll(-SCROLL_AMOUNT)
                        last_action_time = current_time
                        
                    elif current_emotion == 'surprise':
                        print("Emotion: Surprise -> Action: Scrolling Up")
                        pyautogui.scroll(SCROLL_AMOUNT)
                        last_action_time = current_time
                        
            except Exception as e:
                # Fail silently to avoid spamming the console if faces are momentarily lost
                pass

        # --- UI/HUD Overlay ---
        
        # Display the currently detected emotion
        cv2.putText(frame, f"Emotion: {current_emotion.capitalize()}", (30, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)
        
        # Calculate and display the cooldown status
        time_since_last = time.time() - last_action_time
        if time_since_last > COOLDOWN_TIME:
            status = "READY"
            color = (0, 255, 0)  # Green
        else:
            status = f"COOLDOWN ({COOLDOWN_TIME - time_since_last:.1f}s)"
            color = (0, 0, 255)  # Red
            
        cv2.putText(frame, f"Status: {status}", (30, 90), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2, cv2.LINE_AA)

        # Show the video feed
        cv2.imshow('Jedi Mind Trick Interface', frame)

        # Graceful exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting Jedi Mind Trick Engine...")
            break

    # Cleanup resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
