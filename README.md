# Open DDM 

A Python package to analyse an image sequence and measure diffusion properties through Fourier techniques.

## Installation for developers

```bash
git clone git@github.com:koenderinklab/ddmPilotCode.git ddm
cd ddm
conda env create -f env.yml
conda activate ddm_env
pip install -e .[dev]
``` 

### Running tests

To run the test, execute in the root of repository
```bash
pytest
```

## Data processing workflow

```{mermaid}

%%{init: {'theme': 'base'}}%%
flowchart TB

    id1(Microscope) .-> Data
    Data

    Data -->|".nd2 | .lif | .tiff"| Import(Import data)
    Import -->|"xarray (delayed)"| Fourier(Fourier analysis)
    Data --> Track(pyTrack)

    Fourier -->|np.ndarray| Fit(Fitting)
    Fit -->|np.ndarray| Plot(Plotting)
    
    Fourier -->|np.ndarray| Export(Export data)
    Fit -->|np.ndarray| Export
    Plot -->|mpl.fig| Export

    Export -->|"pickle | .csv | .png"| R(Results)    
    Track --> R    


    subgraph Personal Computer
    Import
    Fourier
    Fit
    Plot
    Export
    Track
    end
```

## License

Copyright 2022 Technische Universiteit Delft

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.