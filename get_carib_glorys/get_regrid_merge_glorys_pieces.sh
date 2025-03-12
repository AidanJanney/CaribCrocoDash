#!/bin/bash -l
#PBS -N get_regrid_merge_glorys_pieces
#PBS -A p93300012
#PBS -l select=1:ncpus=32:mem=100GB
#PBS -l walltime=5:00:00
#PBS -q main
#PBS -m abe

module purge
module load conda
conda activate CrocoDash

echo "Starting job at `date`"
echo "Retrieving Data from RDA"
python /glade/work/ajanney/CaribCrocoDash/get_carib_glorys/get_glorys_pieces.py

echo "Regridding Data"
python /glade/work/ajanney/CaribCrocoDash/get_carib_glorys/regrid_glorys_pieces.py

echo "Merging Data"
python /glade/work/ajanney/CaribCrocoDash/get_carib_glorys/merge_glorys_pieces.py