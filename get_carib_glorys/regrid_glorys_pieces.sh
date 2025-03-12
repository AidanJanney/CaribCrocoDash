#!/bin/bash -l
#PBS -N regrid_glorys_pieces
#PBS -A p93300012
#PBS -l select=1:ncpus=4:mem=30GB
#PBS -l walltime=5:00:00
#PBS -q main
#PBS -m abe

module purge
module load conda
conda activate CrocoDash

echo "Starting job at `date`"
python /glade/work/ajanney/DataAccess/Glorys_RDA/regrid_glorys_pieces.py