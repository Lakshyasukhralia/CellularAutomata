'''try:
    import Image
except ImportError:
    Image = None

try:
    from PIL import Image
except ImportError:
    Image = None


try:
    assert Image is not None
except AssertionError:
    print("This script requires pillow. Please install with: pip install pillow")
    exit()

try:
    import numpy
except ImportError:
    print("This script requires numpy. Please install with: pip install numpy")
    exit()

import math
import sys
import timeit


def normalizeArray(a):
    """
    Normalize the given array to values between 0 and 1.
    Return a numpy array of floats (of the same shape as given)
    """
    w, h = a.shape
    minval = a.min()
    if minval < 0:  # shift to positive...
        a = a + abs(minval)
    maxval = a.max()  # THEN, get max value!
    new_a = numpy.zeros(a.shape, 'd')
    for x in range(0, w):
        for y in range(0, h):
            new_a[x, y] = float(a[x, y]) / maxval
    return new_a


def correlation(input, match):
    """
    Calculate the correlation coefficients between the given pixel arrays.
    input - an input (numpy) matrix representing an image
    match - the (numpy) matrix representing the image for which we are looking
    """
    t = timeit.Timer()
    assert match.shape < input.shape, "Match Template must be Smaller than the input"
    c = numpy.zeros(input.shape)  # store the coefficients...
    mfmean = match.mean()
    iw, ih = input.shape  # get input image width and height
    mw, mh = match.shape  # get match image width and height

    print("Computing Correleation Coefficients...")
    start_time = t.timer()

    for i in range(0, iw):
        for j in range(0, ih):

            # find the left, right, top
            # and bottom of the sub-image
            if i-mw/2 <= 0:
                left = 0
            elif iw - i < mw:
                left = iw - mw
            else:
                left = i

            right = left + mw

            if j - mh/2 <= 0:
                top = 0
            elif ih - j < mh:
                top = ih - mh
            else:
                top = j

            bottom = top + mh

            # take a slice of the input image as a sub image
            sub = input[left:right, top:bottom]
            assert sub.shape == match.shape, "SubImages must be same size!"
            localmean = sub.mean()
            temp = (sub - localmean) * (match - mfmean)
            s1 = temp.sum()
            temp = (sub - localmean) * (sub - localmean)
            s2 = temp.sum()
            temp = (match - mfmean) * (match - mfmean)
            s3 = temp.sum()
            denom = s2*s3
            if denom == 0:
                temp = 0
            else:
                temp = s1 / math.sqrt(denom)

            c[i, j] = temp

    end_time = t.timer()

    return c


def main(f1, f2, output_file="CORRELATION.jpg"):

    """ open the image files, and compute their correlation """
    #im1 = Image.open(f1).convert('L')
    #im2 = Image.open(f2).convert('L')
    img1 = cv2.imread('image.jpg',0)
    im2 = cv2.imread('test.png',0)

    # Convert from Image to Numpy array conversion
    f = numpy.asarray(im1)
    w = numpy.asarray(im2)
    corr = correlation(f, w)
    c = Image.fromarray(numpy.uint8(normalizeArray(corr) * 255))
    c.save(output_file)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print('USAGE: python correlation <image file> <match file>')
'''
