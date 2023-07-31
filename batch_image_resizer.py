from PIL import Image
import os


def resize_images_in_folder(default_width):
    folder_path = input("Enter the folder path: ")

    # Check if the folder path is valid
    if not os.path.exists(folder_path):
        print("Invalid folder path.")
        return

    try:
        default_width = int(default_width)
    except ValueError:
        print("Invalid input for default width.")
        return

    # Create a new folder for resized images inside the provided folder
    resized_folder_path = os.path.join(folder_path, "resized_images")
    os.makedirs(resized_folder_path, exist_ok=True)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is an image
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            try:
                image = Image.open(file_path)
                width_percent = (default_width / float(image.size[0]))
                new_height = int((float(image.size[1]) * float(width_percent)))
                new_image = image.resize(
                    (default_width, new_height), Image.LANCZOS)

                new_file_path = os.path.join(resized_folder_path, filename)
                new_image.save(new_file_path)

                print(
                    f"Resized {filename} -> {os.path.join('resized_images', filename)}")
            except Exception as e:
                print(f"Error resizing {filename}: {e}")

    print("Image resizing complete. Resized images are saved in the 'resized_images' folder.")


# Example usage
if __name__ == "__main__":
    default_width = input("Enter default image width: ")
    resize_images_in_folder(default_width)
