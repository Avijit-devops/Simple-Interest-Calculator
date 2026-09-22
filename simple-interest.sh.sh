#!/bin/bash
# Simple Interest Calculator

echo "Enter the Principal amount:"
read p
echo "Enter the Rate of Interest (% per year):"
read r
echo "Enter the Time period in years:"
read t

# Calculate Simple Interest
si=$(echo "scale=2; ($p * $t * $r) / 100" | bc)
total=$(echo "scale=2; $p + $si" | bc)

echo "-----------------------------------"
echo "Simple Interest: $si"
echo "Total Amount: $total"
echo "-----------------------------------"