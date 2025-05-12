#!/bin/bash -l
#PBS -N process-forcings-gio-croc-carib
#PBS -A p93300012
#PBS -l select=1:ncpus=32:mem=128GB
#PBS -l walltime=00:30:00
#PBS -q main
#PBS -m abe

module purge
module load conda
conda activate CrocoDash

echo "Starting job at `date`"
python /glade/work/ajanney/CaribCrocoDash/test_notebooks/Gio-CrocCarib12.py