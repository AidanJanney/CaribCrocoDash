#!/bin/bash -l
#PBS -N process-forcings-gio-croc-carib
#PBS -A p93300012
#PBS -l select=1:ncpus=4:mem=256GB
#PBS -l walltime=5:00:00
#PBS -q main
#PBS -m abe

module purge
module load conda
conda activate CrocoDash

echo "Starting job at `date`"
python /glade/work/ajanney/CaribCrocoDash/test_notebooks/Gio-CrocCarib12.py