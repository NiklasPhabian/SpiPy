# Test Data Files

This directory contains test data for the SpiPy package.

## Files in Repository (via Git LFS)

Small test data files suitable for CI/CD:

- **lut_sentinel2b_b2to12_3um_dust.mat** (70 MB)
  - Lookup table for Sentinel-2B bands 2-12 with dust parameters
  - Essential for all Sentinel-2 tests
  - Also available on Zenodo (see below)

- **sentinel_r_subset.nc** (2.85 MB)
  - Small spatial subset (50×50 pixels) of full reflectance data
  - For quick integration tests

- **sentinel_r0_subset.nc** (1.44 MB)
  - Small spatial subset (50×50 pixels) of background reflectance
  - For quick integration tests

## Large Files (Download from Zenodo)

Full-resolution test data available on Zenodo:

### Lookup Tables
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18701286.svg)](https://doi.org/10.5281/zenodo.18701286)

- **LUT_MODIS.mat** (537 MB)
  - MODIS lookup table generated from Mie-scattering theory
  - Download: https://zenodo.org/records/18701286/files/LUT_MODIS.mat

- **lut_sentinel2b_b2to12_3um_dust.mat** (70 MB)
  - Sentinel-2B lookup table (also in repository via LFS)
  - Download: https://zenodo.org/records/18701286/files/lut_sentinel2b_b2to12_3um_dust.mat

### Test Imagery
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18704072.svg)](https://doi.org/10.5281/zenodo.18704072)

- **sentinel_r.nc** (1.4 GB)
  - Full spatial resolution (921×1347 pixels) Sentinel-2 reflectance data
  - 9 spectral bands, 2 time steps
  - Download: https://zenodo.org/records/18704072/files/sentinel_r.nc

- **sentinel_r0.nc** (705 MB)
  - Full spatial resolution background reflectance
  - Download: https://zenodo.org/records/18704072/files/sentinel_r0.nc

## Usage

### For Development

The subset files are sufficient for most development and testing:

```python
import xarray as xr
import spires

# Use subset files (in repository)
r = xr.open_dataset('tests/data/sentinel_r_subset.nc')
r0 = xr.open_dataset('tests/data/sentinel_r0_subset.nc')
lut = spires.LutInterpolator('tests/data/lut_sentinel2b_b2to12_3um_dust.mat')
```

### For Full Tests

To run tests with full-resolution data, download from Zenodo:

```bash
cd tests/data

# Download lookup tables
curl -L -o LUT_MODIS.mat https://zenodo.org/records/18701286/files/LUT_MODIS.mat

# Download full test imagery (large!)
curl -L -o sentinel_r.nc https://zenodo.org/records/18704072/files/sentinel_r.nc
curl -L -o sentinel_r0.nc https://zenodo.org/records/18704072/files/sentinel_r0.nc
```

Or use the provided helper script:
```bash
# Download all large test data files
python scripts/download_test_data.py --all

# Download only specific datasets
python scripts/download_test_data.py --luts
python scripts/download_test_data.py --imagery
```

## CI/CD Behavior

GitHub Actions:
- Uses subset files by default (fast, no quota issues)
- Skips tests requiring LUT_MODIS.mat (MODIS-specific tests)
- Can be configured to download full files from Zenodo if needed

## Citation

If you use these datasets in your research, please cite:

```bibtex
@dataset{bair2026spires_luts,
  author       = {Bair, Edward and Dozier, Jeff},
  title        = {{SPIRES} Snow Reflectance Lookup Tables},
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18701286},
  url          = {https://doi.org/10.5281/zenodo.18701286}
}

@dataset{griessbaum2026sentinel2_testdata,
  author       = {Griessbaum, Niklas},
  title        = {Sentinel-2 reflectance data for testing the {SpiPy} implementation of the {SPIRES} algorithm},
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18704072},
  url          = {https://doi.org/10.5281/zenodo.18704072}
}
```

And the original SPIRES algorithm:
```bibtex
@article{bair2021snow,
  title={Snow Property Inversion From Remote Sensing (SPIReS): A Generalized Multispectral Unmixing Approach With Examples From MODIS and Landsat 8 OLI},
  author={Bair, Edward H and Stillinger, Thomas and Dozier, Jeff},
  journal={IEEE Transactions on Geoscience and Remote Sensing},
  volume={59},
  number={9},
  pages={7270--7284},
  year={2021},
  doi={10.1109/TGRS.2020.3040124}
}
```
