import numpy as np
import matplotlib.pyplot as plt

def generate_synthetic_counts(T=40, peak=50, noise_std=2.0, seed=42):
    """
    Generate a simple epidemic-like synthetic time series:
    - T time points
    - unimodal (rise then fall) using a Gaussian bump
    - small Gaussian noise added, then rounded to integers and clipped at 0
    """
    rng = np.random.default_rng(seed)
    t = np.arange(T)
    center = T // 2
    width = T / 6.0

    # Smooth bell-shaped curve
    curve = peak * np.exp(-0.5 * ((t - center) / width) ** 2)

    # Add small Gaussian noise and convert to non-negative integers
    curve_noisy = curve + rng.normal(0, noise_std, size=T)
    counts = np.round(np.clip(curve_noisy, 0, None)).astype(int)
    return t, counts

def laplace_mechanism(counts, epsilon, sensitivity=1.0, seed=123):
    """
    Apply the Laplace mechanism independently to each time point:
        x_tilde = x + Lap(0, b) where b = sensitivity / epsilon
    """
    rng = np.random.default_rng(seed)
    b = sensitivity / epsilon
    noise = rng.laplace(loc=0.0, scale=b, size=len(counts))
    noisy = counts + noise
    # Optionally clip negatives to 0 for display
    noisy_clipped = np.clip(noisy, 0, None)
    return noisy_clipped

def main():
    # 1. Generate synthetic counts
    t, counts = generate_synthetic_counts(T=40, peak=50, noise_std=2.0, seed=42)

    # 2. Choose epsilon values (privacy levels)
    epsilons = [0.2, 1.0, 5.0]
    noisy_series = {eps: laplace_mechanism(counts, epsilon=eps, sensitivity=1.0, seed=123)
                    for eps in epsilons}

    # 3. Create 2x2 grid of subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()

    # Panel 1: original only
    ax0 = axes[0]
    ax0.plot(t, counts, marker='o', linestyle='-', linewidth=2)
    ax0.set_title('Original synthetic counts')
    ax0.set_xlabel('Time')
    ax0.set_ylabel('Count')

    # Panels 2–4: original + noisy for each epsilon
    for ax, eps in zip(axes[1:], epsilons):
        ax.plot(t, counts, marker='o', linestyle='-', linewidth=2, label='Original')
        ax.plot(t, noisy_series[eps], marker='o', linestyle='--', label=f'Noisy (epsilon = {eps})')
        ax.set_title(f'Original vs Laplace noisy (epsilon = {eps})')
        ax.set_xlabel('Time')
        ax.set_ylabel('Count')
        ax.legend()

    fig.suptitle('Effect of Laplace Noise on Synthetic Counts for Different Privacy Levels',
                 fontsize=14)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('laplace_noise_timeseries_grid.png', dpi=300)
    plt.close()

if __name__ == "__main__":
    main()
