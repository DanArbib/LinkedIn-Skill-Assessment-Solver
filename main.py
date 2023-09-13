import pyautogui
import easyocr
from tasks.gpt import generate_answer
import os
import datetime


def adjust_screen():
    print("Please specify the crop size as a percentage for each side of the screenshot.")
    print("For example, if you want to crop 20% from each side, you can enter '0.2' for each side.")
    print("If you don't want to crop a particular side, enter '0' for that side.")

    while True:
        crop_top = float(input("Enter the top crop percentage (0 to 1): "))
        crop_bottom = float(input("Enter the bottom crop percentage (0 to 1): "))
        crop_left = float(input("Enter the left crop percentage (0 to 1): "))
        crop_right = float(input("Enter the right crop percentage (0 to 1): "))

        # Capture the screen
        screenshot = pyautogui.screenshot()

        # Calculate cropping dimensions
        width, height = screenshot.size
        left = int(crop_left * width)
        top = int(crop_top * height)
        right = int((1 - crop_right) * width)
        bottom = int((1 - crop_bottom) * height)

        # Crop the screen
        screenshot = screenshot.crop((left, top, right, bottom))

        # Display the cropped image using PIL
        screenshot.show()


        continue_process = input("Is the captured area correct? Press 'Y' to continue or 'X' to correct the area: ")
        if continue_process.lower() == 'y':
            return crop_top, crop_bottom, crop_left, crop_right



def capture_and_ocr(full_path, i, crop_top=0, crop_bottom=0, crop_left=0, crop_right=0):

    # Capture the screen
    screenshot = pyautogui.screenshot()
    image_path = f"{full_path}/{i}.png"
    screenshot.save(image_path)

    # Calculate cropping dimensions
    width, height = screenshot.size
    left = int(crop_left * width)
    top = int(crop_top * height)
    right = int((1 - crop_right) * width)
    bottom = int((1 - crop_bottom) * height)

    # Crop the screen
    screenshot = screenshot.crop((left, top, right, bottom))

    # Save the image
    screenshot.save(image_path)

    # Initialize the easyocr reader
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)

    # Extract and print the recognized text
    recognized_text = ""
    for (bbox, text, prob) in result:
        recognized_text += text + " "
    return recognized_text


def trim_text(recognized_text, crop_start, crop_ends):
    start_idx = recognized_text.find(crop_start)
    end_idx = recognized_text.find(crop_ends)

    if start_idx != -1 and end_idx != -1:
        trimmed_text = recognized_text[start_idx:end_idx]
        return trimmed_text.strip()  # Remove leading and trailing whitespace
    else:
        return recognized_text


i = 1
CROP_START = "assessment"
CROP_ENDS = "Something wrong"


if __name__ == '__main__':

    current_datetime = datetime.datetime.now()
    date_time_string = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

    # Question area
    crop_top, crop_bottom, crop_left, crop_right = adjust_screen()

    # Question dir
    full_path = os.path.join('questions', date_time_string)
    os.makedirs(full_path)

    print("After you start the quiz")
    while True:
        input("Press enter to read the question")

        # Getting the question
        recognized_text = capture_and_ocr(full_path, i, crop_top, crop_bottom, crop_left, crop_right)

        # Trimming the question
        trimmed_text = trim_text(recognized_text, CROP_START, CROP_ENDS)
        print('Linkedin questions: ', trimmed_text)

        # Getting the answer
        answer = generate_answer(trimmed_text)
        print('Correct answer: ', answer)

        i += 1



