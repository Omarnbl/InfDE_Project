from typing import Dict, List, Tuple, Any
from mask_extractor.MaskExtractor import MaskExtractor
import numpy as np
import logging
def extract_all_masks(base_path: str) -> Dict[str, Any]:
    """
    Extract all masks from the dataset using MaskExtractor.
    
    Args:
        base_path (str): Path to the base directory containing the data
        
    Returns:
        Dict[str, Any]: Dictionary containing all processed masks organized by case
    """
    # Initialize the mask extractor
    extractor = MaskExtractor(base_path)
    
    # Process and extract all masks
    print("Starting mask extraction...")
    all_masks = extractor.process()
    
    # Print summary of extracted masks
    num_cases = len(all_masks)
    if num_cases > 0:
        sample_case = next(iter(all_masks))
        num_slices = len(all_masks[sample_case]['standard_mask'])
        print(f"\nExtraction complete:")
        print(f"- Total cases processed: {num_cases}")
        print(f"- Slices per case: {num_slices}")
        print(f"- Available mask types: {list(all_masks[sample_case].keys())}")
    else:
        print("No masks were extracted!")
        
    return all_masks

def get_random_mask_slice(all_masks: Dict[str, Any], mask_type) -> np.ndarray:
    # Select a random case
    if mask_type == "infarction_masks":
        keys_with_infarction = [key for key in all_masks.keys() if 'P' in key]
        case_id = np.random.choice(list(keys_with_infarction))

    else: 
        case_id = np.random.choice(list(all_masks.keys()))


    # log the selected case ID
    logging.debug(f"Selected case ID: {case_id}")
    
    case_masks = all_masks[case_id]
    
    # Select a random mask type
    mask = case_masks[mask_type]
    # Select a random slice
    slice_idx = np.random.randint(len(mask))
    mask_slice = mask[slice_idx]
    
    return mask_slice

def save_masks_to_npy(all_masks: Dict[str, Any], np_data_path: str) -> None:
    """
    Save the extracted masks to an npy file.
    
    Args:
        all_masks (Dict[str, Any]): Dictionary containing all processed masks organized by case
        np_data_path (str): Path to save the npy file
    """
    np.save(np_data_path, all_masks)
    print(f"Saved masks to {np_data_path}")