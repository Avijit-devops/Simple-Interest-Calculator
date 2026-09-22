# Simple Interest Calculator

A simple, user-friendly script designed to compute the simple interest and total accrued amount based on principal, annual interest rate, and time duration.

---

## Overview

This tool implements the standard financial formula for simple interest calculations:

$$\text{Simple Interest (SI)} = \frac{P \times R \times T}{100}$$

Where:
- **P** = Principal amount (initial sum of money)
- **R** = Annual interest rate (in percentage)
- **T** = Time period (in years)

---

## Features

- Computes simple interest instantly.
- Calculates the final total amount ($\text{Principal} + \text{Interest}$).
- Handles decimal and integer values for rates and time.

---

## Inputs & Outputs

### Inputs
| Parameter | Description | Data Type |
|---|---|---|
| `principal` | Initial amount deposited or borrowed | Float / Integer |
| `rate` | Annual interest rate (e.g., 5 for 5%) | Float / Integer |
| `time` | Duration in years | Float / Integer |

### Outputs
| Output | Description |
|---|---|
| `Interest` | The calculated interest earned or owed |
| `Total Amount` | The sum of principal and earned interest |

---

## Example Usage

### Input
- Principal: `$1000`
- Rate: `5%`
- Time: `2 years`

### Calculation
$$\text{SI} = \frac{1000 \times 5 \times 2}{100} = 100$$

### Output
- **Simple Interest:** `$100.00`
- **Total Amount:** `$1100.00`

---

## License

This project is licensed under the Apache 2.0 / MIT License.