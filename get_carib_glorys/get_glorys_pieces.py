from CrocoDash.data_access import glorys as gl
import os
## Testing with Panama Domain Because it's small
# --minimum-longitude 261.26 --maximum-longitude 324.74 --minimum-latitude -6.24 --maximum-latitude 32.24

'''
xstart=261.5, # 261.5° E or 98.5° W 
lenx=63, # 35.5° W
ystart=-6, # 6° S
leny=38, # 32° N
'''

lat_min = -6.24
lat_max = 32.24
lon_min = 261.26
lon_max = 324.74

start_date = '2000-01-01'
end_date = '2001-01-01'

step_days = 5

output_dir = "/glade/work/ajanney/CaribCrocoDash/get_carib_glorys/raw_glorys_data"

## Make some helpful dictionary objects for each one
def make_boundary_dicts(lat_min, lat_max, lon_min, lon_max):
    north = {'name':'north', 'lat_min': lat_max, 'lat_max':lat_max, 'lon_min':lon_min, 'lon_max':lon_max}
    south = {'name':'south', 'lat_min': lat_min, 'lat_max':lat_min, 'lon_min':lon_min, 'lon_max':lon_max}
    east = {'name':'east', 'lat_min': lat_min, 'lat_max':lat_max, 'lon_min':lon_max, 'lon_max':lon_max}
    west = {'name':'west', 'lat_min': lat_min, 'lat_max':lat_max, 'lon_min':lon_min, 'lon_max':lon_min}
    boundaries = [north, south, east, west]
    return boundaries

boundaries = make_boundary_dicts(lat_min, lat_max, lon_min, lon_max)

os.makedirs(output_dir, exist_ok=True)

for dir_dict in boundaries:
    gl.get_glorys_rda_piecewise(
        dates = [start_date, end_date],
        lat_min = dir_dict['lat_min'],
        lat_max = dir_dict['lat_max'],
        lon_min = dir_dict['lon_min'],
        lon_max = dir_dict['lon_max'],
        step_days = step_days,
        output_dir=output_dir,
        output_file=f"{dir_dict['name']}_unprocessed.nc"
    )