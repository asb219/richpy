# richpy

[![DOI](https://zenodo.org/badge/1009811476.svg)](https://doi.org/10.5281/zenodo.23856048)

Python interface for the Radiocarbon Inventories of Switzerland database (RICH: [rich.ethz.ch](https://rich.ethz.ch))


## Install

Clone this repository and install the `richpy` package with pip.

```bash
git clone https://github.com/asb219/richpy.git
cd richpy
pip install -e .
```


## Example

Download data for samples that were collected between 2000 and 2015 (inclusive)
and at elevations up to 1200 m a.s.l.

```python
import richpy
data = richpy.get_data(sampling_year=(2000,2015), elevation=(None,1200))
```
