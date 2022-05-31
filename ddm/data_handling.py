def readND2(filename):
    """A function to read in a .nd2 file taken from a Nikon microscope. Has been shown to work for files from our Minicell in the Koenderink lab.
    
    Parameters
    ----------
    filename : string
               the path and name of the .nd2 file which is to be loaded in
    Returns
    -------
    dask array
        array with the image data saved as a dask array. Metadata in the dask array includes the spatial resolution in microns per pixel and the temporal resolution in milliseconds per frame.
    """
    sequence = nd2.imread(filename, xarray = True, dask = True)
    frameT = sequence.metadata['experiment'][0].parameters.periodDiff.avg #this is the time per frame in ms
    scale = sequence.X[1] #this is the microns per pixel
    sequence['T'] = np.arange(len(sequence['T']))*frameT
    sequence.attrs = {'xyScale': float(scale),
                      'tScale': frameT}
    return(sequence)

def readLIF(filename):
    """A function to read in a .lif file taken from a Leica microscope. Has been shown to work for files from our Thunder in the Koenderink lab.
    
    Parameters
    ----------
    filename : string
               the path and name of the .lif file which is to be loaded in
    Returns
    -------
    dask array
        array with the image data saved as a dask array. Metadata in the dask array includes the spatial resolution in microns per pixel and the temporal resolution in milliseconds per frame.
    
    """
    lifSeq = pims.Bioformats('data/21-03-31_ddm.lif', read_mode = 'jpype')
    xscale = lifSeq.metadata.PixelsPhysicalSizeX(0)
    tscale = lifSeq.metadata.PlaneDeltaT(0,1)
    lifXCoords = np.arange(0., lifSeq.shape[1]*xscale, xscale)
    lifYCoords = np.arange(0., lifSeq.shape[2]*xscale, xscale)
    lifTCoords = np.arange(0., lifSeq.shape[0]*tscale, tscale)
    ds = da.from_array(lifSeq)
    sequence = xarray.DataArray(data = ds, dims = ["T", "Y", "X"], 
                                coords = (lifTCoords, lifYCoords, lifXCoords), 
                                attrs = dict(xyScale = xscale, tScale = tscale))
    return sequence