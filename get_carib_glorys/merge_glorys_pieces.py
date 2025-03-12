import os
import xarray as xr
from pathlib import Path
from glob import glob 
import re
from datetime import datetime
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Start File")

def merge_glorys_pieces(
    input_dir=Path(""),
    output_dir=Path(""),
    boundaries=["north", "south", "east","west"]
):
    number_conv = {"south":1,"north":2,"east":3,"west":4}
    
    os.makedirs(output_dir, exist_ok=True)
    
    for boundary in boundaries:
        key_num = number_conv[boundary]
        boundary_path = os.path.join(input_dir,f"forcing_obc_segment_00{key_num}*")
        
        logger.info(f"Opening segment_00{key_num} files")
        dataset_merged=xr.open_mfdataset(boundary_path,decode_times = False, combine = "nested", concat_dim="time",coords='minimal')
        
        output_path = os.path.join(output_dir,f"forcing_obc_segment_00{key_num}.nc")
        dataset_merged.to_netcdf(output_path, format="netcdf4")
        logger.info(f"Saved: {output_path}")
        
        dataset_merged.close()

input_dir = "/glade/work/ajanney/CaribCrocoDash/get_carib_glorys/coarse_regridded_glorys_data"
output_dir = "/glade/work/ajanney/CaribCrocoDash/get_carib_glorys/coarse_final_glorys_data"

merge_glorys_pieces(input_dir=input_dir, output_dir=output_dir)

print("ALL DONE!")