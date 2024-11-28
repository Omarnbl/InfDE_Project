# GP_InfDE

This repository contains the tools and data required for processing cardiac MRI images to analyze infarction and no-reflow regions. Follow the guide below to understand the repository structure and how to use the provided resources.

---

## Repository Structure

- **GP_InfDE/**
  - **Resources/**
    - **Code/**: Contains Python notebooks for data processing
      - `1-Split_NIFTI_Into_Slices.ipynb`
      - `2-Unify_Masks_Values.ipynb`
      - `3-Histogram_Equalization.ipynb`
    - **Data/**: Placeholder for dataset files
      - `<example data files>`
      - `README.md`: Instructions for using the data
  - **Documents/**: Contains Meeting minutes and other documentation
    - **Meeting Minutes/**
      - `Meeting1.pdf`
      - `Meeting2.pdf`
      - `...`
  - **Other Resources/**: Folder for future resources (currently empty)
  - `README.md`: Guide for using the repository

---

## Getting Started

### Step 1: Download the Dataset

1. Click [here to download the dataset](https://drive.google.com/drive/folders/1FBuTpm0AekDZUEfBpTYaYga6CL2XSvS4?usp=drive_link).
2. Extract the folder after downloading. Note the directory path, as it will be required in the notebooks.

---

### Step 2: Process the Data

#### Notebook 1: Split NIFTI into Slices

1. Navigate to `Resources/Code/1-Split_NIFTI_Into_Slices.ipynb`.
2. Open the notebook in your Python environment (e.g., Jupyter Notebook).
3. Set the path to the dataset directory in the first cell:

   ```python
   dataset_path = "your/data/folder/path"
   ```

4. Run all cells sequentially.

**Output**: Creates `.npy` slices for each patient in their respective folders.

---

#### Notebook 2: Unify Mask Values

1. Navigate to `Resources/Code/2-Unify_Masks_Values.ipynb`.
2. Open the notebook in your Python environment.
3. Set the path to the dataset directory in the first cell:

   ```python
   dataset_path = "your/data/folder/path"
   ```

4. Run all cells sequentially.

**Output**:

- Renames and unifies mask values using the following convention:
  - **0**: Background  
  - **1**: Cavity  
  - **2**: Normal Myocardium  
  - **3**: Infarction  
  - **4**: No-Reflow  
- Creates two new directories:
  - `All Train Slices`
  - `All Test Slices`

---

#### Notebook 3: Histogram Equalization

1. Navigate to `Resources/Code/3-Histogram_Equalization.ipynb`.
2. Open the notebook in your Python environment.
3. Set the paths for:
   - **Input folder**: e.g., `All Train Slices` or `All Test Slices`
   - **Output folder**: Specify where the processed slices will be saved.

   ```python
   input_path = "path/to/slices"
   output_path = "path/to/output"
   ```

4. Run all cells sequentially.

**Output**: Applies histogram equalization to the slices and saves them in the specified output folder.

---

## Dependencies

Ensure you have the following installed:

- Python 3.x
- Libraries: `numpy`, `pandas`, `matplotlib`, etc.

To install dependencies, use the following command:

```bash
pip install -r requirements.txt
```

(Include a `requirements.txt` file with the necessary dependencies if not already present.)

---

## Notes

- For dataset-specific instructions, check the `Data/README.md`.

