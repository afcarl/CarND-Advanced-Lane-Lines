

### Camera Calibration

The `camera_calibration` code contains our camera calibration. First we look
for corners in a 9x6 checkerboard. Next we call `calibrateCamera` and
`undistort` before writing out the image. Calibrated images are in
`calibrated_dir`.

The same undistort code is called with the matrix transformation in
`undistort_test_image` for test images. All 8 are included in the IPython
notebook.

Matrix transforms are in `mtx`

### Pipeline (test images)

#### Selecting images

The first time I ran through this pipeline I had selected the wrong selection.
The grader had provided a different and improved `src` and `dst` transformation.
I noticed that the image using my new image selection screened out the other
lanes ( more on that later). An example is provided in the iPython Notebook.

#### Color & Magnitude Thresholds

I experimented with different transformations and thresholds. Things like
Directional, Magntiude, and Grad Y didn't perform at all! I only saw good
results with Grad X or the Yellow/White channel selections (per the
  recommendation of the grader).

I changed the histogram code to greatly decrease the magnitude of the image on
the sides. This was because my previous images had multiple lanes and lots of
noise. In my mind the lanes are at the center of the image and that's where the
histogram should focus. It was effective at keeping the lane marker in other
lanes from being accidentally scanned.


#### Selecting the image.

In the new and improved image transformation, we can see that a bird's-eye view
of the road image now only includes the yellow lane line, and a dashed lane line.

The histogram is produced from the yellow-and-white channel mask that was
combined.

The code for `sliding_windows` and `find_window_centroids` was shown to be in
the udacity coursework. The window finding happens by moving a selection of
windows from the start of the histogram's mean, and moving the window up
by ( 720 px / window count ) to find the next centroid of the image. this
can be used to extrapolate a polynomial curve.

### Pipeline (video)

The video pipeline uses native libraries to select each image from a movie
stream and then push the results into a pipeline. There is a `_pipeline`
function that runs the real code and the pipeline_* functions are meant to
be the abstractions for different hyper parameters.

### Discussion

The pipeline uses a special histogram feature that will greatly reduce what it
sees at the prehiphary of it's vision. The idea is that the lanes we care
about are at the center of the image and not the end.

I took some of the code for finding windows scaling and noticed an error
in the return values for polyfit. If no indexes are found in the right or left
arrays for pixels, I simply don't call polyfit for which an exception is thrown
and instead return a tuple of `(0,0,0)`.

#### Challenge Video

The video output returns some errors when the lane markers get too faint and
the car can't really find it's way so some of the lanes get very wide. In
another, the polynomials get confused and so the lane edges get tossed around.
The widly dancing edges usually happen when the edges get lost

#### Harder Challenge Image

The image gets bleached out so hard sometimes the car will not follow the lanes
no matter what masking I put in. Still, the masking I would use seems to have a
much stronger degree for the curves needed. The image transformation is also
probably not going to work out because the road is so much more curvy that
looking too far in ahead will run us off the road.

Also, the grass on the right hand side at the beginning are as yellow as the
lane markers.

Possible solutions could be to have a dynamic selection depending on how fast
the car is going and how hard the poly-fit `rpoly` and `lpoly` lane edges are
turning.
