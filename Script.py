from osgeo import gdal

def split_raster_by_pixel(input_raster, out_dir, output_prefix, tile_width, tile_height):
    """Splits a raster into tiles of specified pixel dimensions.

    Args:
        input_raster (str): Path to the input raster file.
        output_prefix (str): Prefix for the output tile filenames.
        tile_width (int): Width of each tile in pixels.
        tile_height (int): Height of each tile in pixels.
    """
    raster = gdal.Open(input_raster)
    if raster is None:
        raise IOError(f"Could not open {input_raster}")

    xsize = raster.RasterXSize
    ysize = raster.RasterYSize

    for i in range(0, xsize, tile_width):
        for j in range(0, ysize, tile_height):
            output_filename = os.path.join(out_dir, f"{output_prefix}_{i}_{j}.tif")
            gdal.Translate(output_filename, raster, srcWin=[i, j, tile_width, tile_height])

    raster = None
    
split_raster_by_pixel("100_framework.tif", 'framwork_100_split_raster', 'framework', 1000, 1000)
