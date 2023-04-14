import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import subprocess

def generate_entropy_graph(file_path, output_file):
    # Run binwalk with the -E flag to get entropy data
    binwalk_output = subprocess.check_output(["binwalk", "-E", file_path])
    
    # Process the output to extract entropy values
    lines = binwalk_output.decode("utf-8").split("\n")
    entropy_values = []

    for line in lines:
        tokens = line.split()
        if len(tokens) > 1 and tokens[1].replace(".", "").isdigit():
            entropy_values.append(float(tokens[1]))

    # Generate the entropy graph using matplotlib
    plt.plot(entropy_values)
    plt.xlabel("Block Index")
    plt.ylabel("Entropy")
    plt.title("Entropy Graph")
    plt.savefig(output_file)
    plt.show()

if __name__ == "__main__":
    input_file = "image.tar"
    output_file = "output.png"
    
    generate_entropy_graph(input_file, output_file)
