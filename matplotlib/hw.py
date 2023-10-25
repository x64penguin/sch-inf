from matplotlib import pyplot as plt
import numpy as np


def linear_intersect(f1, f2):  # task 1
    x = np.arange(-10, 11)

    y1 = [f1(x_val) for x_val in x]
    y2 = [f2(x_val) for x_val in x]

    plt.plot(x, y1, label='f1')
    plt.plot(x, y2, label='f2')

    plt.xlabel('x')
    plt.ylabel('y')

    plt.grid(True)

    plt.legend()

    plt.show()


def plot_four_areas():  # task 2
    x = np.linspace(-10, 10, 100)

    y1 = np.cos(x)
    y2 = np.sin(x)
    y3 = x**2
    y4 = 2/x

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8))

    ax1.plot(x, y1)
    ax1.set_title('cos(x)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.grid(True)

    ax2.plot(x, y2)
    ax2.set_title('sin(x)')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.grid(True)

    ax3.plot(x, y3)
    ax3.set_title('x^2')
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.grid(True)

    ax4.plot(x, y4)
    ax4.set_title('2/x')
    ax4.set_xlabel('x')
    ax4.set_ylabel('y')
    ax4.grid(True)

    plt.tight_layout()
    plt.show()


def plot_bar_chart():
    v = np.random.rand(7)

    plt.bar(np.arange(7), v)

    for i, value in enumerate(v):
        plt.text(i, value+0.01, str(round(value, 2)), ha='center')

    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    plot_bar_chart()
