# Game of Thrones Character Network Visualization and Analysis

This project aims to analyze and visualize the interactions between characters in the "A Song of Ice and Fire" series by George R.R. Martin. Using network analysis techniques and various visualization tools, we create an interactive and informative representation of the character network.

## Project Structure

- **data/**
  - `asoiaf-all-nodes.csv`: Contains the nodes (characters) of the network.
  - `asoiaf-all-edges.csv`: Contains the edges (interactions) of the network.

- **scripts/**
  - `data_processing.py`: Python script for data processing and network construction.

- **visualization/**
  - `index.html`: HTML file for the interactive visualization using Sigma.js.
  - `data.json`: JSON file containing the network data for visualization.

- **docs/**
  - `thesis_report.docx`: Complete thesis report including methodology, data analysis, and results.

## Getting Started

### Prerequisites

To run this project, you need to have the following software installed:

- Python 3.x
- Gephi
- Web browser (for interactive visualization)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/got-character-network.git
   cd got-character-network

Install the required Python packages
pip install pandas networkx

Steps to Reproduce the Project
Run the data_processing.py script to process the data and construct the network:
python scripts/data_processing.py
This script will read the asoiaf-all-nodes.csv and asoiaf-all-edges.csv files, clean and normalize the data, and construct a network using NetworkX. The processed data will be saved in a format suitable for further analysis.
Network Analysis with Gephi:
Open gephi_analysis.gephi with Gephi.
Import the processed data (data.json) into Gephi.
Perform community detection and calculate centrality measures using Gephi's built-in algorithms.
Export the analyzed network data as data.json.
Interactive Visualization:

Open visualization/index.html in a web browser to view the interactive network visualization.
The visualization uses Sigma.js to dynamically display the network, allowing for zooming, panning, and interaction with the nodes and edges.

Methodology
Data Collection:
Character interactions were manually extracted from the "A Song of Ice and Fire" series.
Data Processing:
Python was used to clean and normalize the data, and construct the network using NetworkX.
Network Analysis:
Gephi was used for community detection and centrality measures.
Visualization:
Sigma.js was used to create an interactive visualization of the network.

Results
The analysis revealed key characters with high centrality measures, such as Jon Snow, Cersei Lannister, and Tyrion Lannister.
Community detection identified distinct clusters corresponding to major factions and families.
The interactive visualization allows users to explore the network dynamically.

Acknowledgements
I would like to thank my advisor, Dr. Öğr. Üyesi [Danışmanınızın Adı], for his guidance and support. I also appreciate the help and suggestions from my friends and colleagues throughout this project.

License
This project is licensed under the MIT License. See the LICENSE file for details.

You can copy this content into your README.md file in your project repository. Adjust any specific details, such as the repository URL and any specific instructions or acknowledgments, to fit your project requirements.


