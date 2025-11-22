# DP-Laplace-Noise-Demo

Demonstration of different levels of input perturbation for differential privacy using the Laplace Mechanism.

## Overview

This project demonstrates input perturbation for differential privacy by injecting Laplace noise into synthetic time series data.

## Features

- Generates a 2×2 grid of plots:
  - Original (epidemic curve)
  - Laplace noise, ε = 0.2
  - Laplace noise, ε = 1.0
  - Laplace noise, ε = 5.0

## Visual Examples

![Grid of Laplace Noise Plots](plots/laplace_grid.png)

## How It Works

1. **Generate synthetic data** simulating an epidemic curve.
2. **Apply Laplace noise** at three privacy levels.
3. **Visualize privacy–utility tradeoffs** using grid plots.

## Usage

## References

- [Differential Privacy](https://en.wikipedia.org/wiki/Differential_privacy)
