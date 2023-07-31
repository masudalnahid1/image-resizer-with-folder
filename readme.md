# Image Resizer with Folder

The "Image Resizer with Folder" is a Python script that allows you to resize images while maintaining their aspect ratio. It creates a new folder inside the provided folder and stores the resized images with the same names as the original images.

## How it works

The script prompts the user for the default width of the images and the folder path containing the images to be resized. It then resizes all the images in the folder, preserving their aspect ratio, and saves the resized images in a new folder named "resized_images" inside the provided folder.

The script supports various image formats, including PNG, JPEG, GIF, and BMP.

## Prerequisites

Before running the script, you need to have the following:

- Python: The script is written in Python and requires Python to be installed on your system. You can download Python from the official website: [python.org](https://www.python.org/downloads/)

- Pillow Library: The script uses the Pillow library to perform image resizing. You can install Pillow using pip:

```sh
pip install pillow
```

## How to run the script

1. Download the "image_resizer_with_folder.py" file from the repository.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script by executing the following command:

```sh
python batch_image_resizer.py

```

4. Follow the prompts to enter the default image width and the folder path containing the images to be resized.

5. The script will create a new folder named "resized_images" inside the provided folder and save the resized images in it.

## Important Note

- The script assumes the folder contains image files with extensions like .png, .jpg, .jpeg, .gif, and .bmp. Ensure that you have backed up your images or used it on a test folder before applying it to important image directories.

- For best results, it is recommended to use images with a resolution higher than the desired width to avoid loss of image quality during resizing.

- If there are any issues or errors during the resizing process, the script will provide feedback with error messages.

- The resized images will have the same names as the original images and will be stored in the "resized_images" folder inside the provided folder.

## License

This script is open-source and released under the [MIT License](LICENSE).

Feel free to use, modify, and distribute this script following the terms of the MIT License.
