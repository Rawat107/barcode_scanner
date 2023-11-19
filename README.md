# Barcode Scanner

This Python script utilizes OpenCV, imutils, videostream, and pyzbar libraries to create a versatile barcode scanner capable of real-time decoding of various barcode types, with a focus on QR codes. The decoded information is logged into a CSV file for easy tracking and analysis.

## Usage

### Prerequisites

- Python 3.x
- Install required libraries:

```bash
pip install opencv-python imutils pyzbar
```
### Running the Script

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-barcode-scanner-repo.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd your-barcode-scanner-repo
    ```

3. **Run the script:**

    ```bash
    python barcode_scanner.py
    ```

    Optional argument for specifying the output CSV file:

    ```bash
    python barcode_scanner.py --output your_output_file.csv
    ```

4. **Terminate the script by pressing 'q'.**

## Script Details

- The script starts a video stream, capturing frames and resizing them for processing.
  
- Barcodes are detected and decoded using the pyzbar library.

- Detected barcodes are drawn on the frame with bounding boxes, and information is displayed.

- The script logs the decoded barcode information along with timestamps into a CSV file.

- Press 'q' to quit the script.

## Author

Vaibhav Rawat

Note: This project was inspired and developed based on knowledge gained from PyImageSearch.

