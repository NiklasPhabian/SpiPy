# Test Data Files

This directory contains test data for the SpiPy package.

## Files in Repository (via Git LFS)

Small test data files suitable for CI/CD:

- **lut_sentinel2b_b2to12_3um_dust.mat** (70 MB)
  - Lookup table for Sentinel-2B bands 2-12 with dust parameters
  - Essential for all Sentinel-2 tests

- **sentinel_r_subset.nc** (2.85 MB)
  - Small spatial subset (50×50 pixels) of full reflectance data
  - For quick integration tests

- **sentinel_r0_subset.nc** (1.44 MB)
  - Small spatial subset (50×50 pixels) of background reflectance
  - For quick integration tests

## Large Files (Download from Zenodo)

Full-resolution test data available on Zenodo:

- **LUT_MODIS.mat** (537 MB)
  - MODIS lookup table
  - TODO: Upload to Zenodo and add DOI here

- **sentinel_r.nc** (1.4 GB)
  - Full spatial resolution (921×1347 pixels) reflectance data
  - TODO: Upload to Zenodo and add DOI here

- **sentinel_r0.nc** (705 MB)
  - Full spatial resolution background reflectance
  - TODO: Upload to Zenodo and add DOI here

## Usage

### For Development

The subset files are sufficient for most development and testing:

```python
import xarray as xr
import spires

# Use subset files (in repository)
r = xr.open_dataset('tests/data/sentinel_r_subset.nc')
r0 = xr.open_dataset('tests/data/sentinel_r0_subset.nc')
```

### For Full Tests

To run tests with full-resolution data:

1. Download files from Zenodo (see links above)
2. Place in `tests/data/` directory
3. Files are gitignored and won't be committed

```bash
# Example (replace with actual Zenodo URLs)
cd tests/data
curl -L -o LUT_MODIS.mat https://zenodo.org/record/XXXXX/files/LUT_MODIS.mat
curl -L -o sentinel_r.nc https://zenodo.org/record/XXXXX/files/sentinel_r.nc
curl -L -o sentinel_r0.nc https://zenodo.org/record/XXXXX/files/sentinel_r0.nc
```

## CI/CD Behavior

GitHub Actions:
- Uses subset files by default (fast, no quota issues)
- Skips tests requiring LUT_MODIS.mat (MODIS-specific tests)
- Can be configured to download full files from Zenodo if needed
