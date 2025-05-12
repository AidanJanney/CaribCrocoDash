# # CrocCarib12 Using Giovanni Seijo-Ellis' Input Grids and Bathymetry from [Seijo-Ellis et al. 2024](https://egusphere.copernicus.org/preprints/2024/egusphere-2024-1378/)

from CrocoDash.grid import Grid

grid = Grid.from_supergrid("/glade/work/ajanney/CaribCrocoDash/CrocCarib_Gio_Input/carib_012_hgrid.nc") 
grid.name = "CrocCaribGio"
# doing something here that I don't remember, look at what processing supergrid does

from CrocoDash.topo import Topo

topo = Topo.from_topo_file(
    grid = grid,
    topo_file_path="/glade/work/ajanney/CaribCrocoDash/CrocCarib_Gio_Input/topo.carib_012v1.SRTM15_V2.4.SmL2.0_C2.0_edited_v3.nc",
    min_depth=9.5,
)

from CrocoDash.vgrid import VGrid
import numpy as np

vgrid = VGrid.from_file("/glade/work/ajanney/CaribCrocoDash/CrocCarib_Gio_Input/vgrid_65L_20200626.nc")

from pathlib import Path

# CESM case (experiment) name
casename = "CrocCaribGio"

# CESM source root (Update this path accordingly!!!)
cesmroot = '/glade/work/ajanney/CESM-versions/CROC_CESM' # Path.home() / "cesm3_0_beta04"
# I grabbed this version from Alper

# Place where all your input files go 
inputdir = Path("/glade/work/ajanney/CrocoDash_Input",casename) # Path.home() / "croc_input" / casename
    
# CESM case directory
caseroot = Path("/glade/work/ajanney/CESM/cases",casename) # Path.home() / "croc_cases" / casename

from CrocoDash.case import Case

case = Case(
    cesmroot = cesmroot,
    caseroot = caseroot,
    inputdir = inputdir,
    ocn_grid = grid,
    ocn_vgrid = vgrid,
    ocn_topo = topo,
    project = 'P93300012', # also can be unspecified if set by user config e.g. export PBS_ACCOUNT=P93300012
    override = True,
)

start_date_iter = "2000-01-01 00:00:00"
end_date_iter = "2021-02-01 00:00:00"

case.configure_forcings(
    date_range = [start_date_iter, end_date_iter],
    tidal_constituents = ['M2', 'S2', 'N2', 'K2', 'K1', 'O1', 'P1', 'Q1', 'MM', 'MF'],
    tpxo_elevation_filepath = "/glade/work/ajanney/CrocoDashData/inputs/tidal_data/h_tpxo9.v1.nc", 
    # original: "/glade/u/home/manishrv/manish_scratch_symlink/inputs_rm6/tidal_data/h_tpxo9.v1.nc",
    tpxo_velocity_filepath = "/glade/work/ajanney/CrocoDashData/inputs/tidal_data/u_tpxo9.v1.nc" 
    # original: "/glade/u/home/manishrv/manish_scratch_symlink/inputs_rm6/tidal_data/u_tpxo9.v1.nc"
)

import subprocess

for key in ['ic', 'east', 'west', 'south', 'north']:
    subprocess.run(['cp',f'/glade/work/ajanney/CrocoDash_Input/glorys_CARIB_testing/{key}_unprocessed.nc','/glade/work/ajanney/CrocoDash_Input/CrocCaribGio/glorys'])

case.process_forcings()