#!/bin/bash
#SBATCH --account=ds2002
#SBATCH --job-name=ds2002_lab10_part2_lolcow
#SBATCH --output=lolcow-jokes-%j-%a.out
#SBATCH --error=lolcow-jokes-%j-%a.err
#SBATCH --time=00:01:00
#SBATCH --partition=standard
#SBATCH --mem=8G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --array=1-10

mkdir -p /scratch/xyb9vz
cd /scratch/xyb9vz

module load miniforge
source activate ds2002
module load apptainer


echo "Running lolcow job: ${SLURM_ARRAY_TASK_ID}"
apptainer run ~/lolcow-latest.sif
