#!/bin/bash

# Define the parameter values to scan
v0_values=(0.1 0.2 0.5)
P_values=(0.2 0.3 0.4 0.5 0.6 0.7 1.0 1.4 2.0)
TT_values=("5e-02" "5e-03" "5e-04" "1e-20")

# Loop over the parameter values
for v0 in "${v0_values[@]}"
do
    for P in "${P_values[@]}"
    do
        for TT in "${TT_values[@]}"
        do
            # Print the current parameter values
            echo "Running script for v0=$v0, P=$P, TT=$TT"

            # Run the Python script with the current parameter values
            python3 m_pickle.py --P $P --v0 $v0 --TT $TT --c_lifespan_pickle True

            # A sleep command to introduce a delay between iterations
            #sleep 1
        done
    done
done

