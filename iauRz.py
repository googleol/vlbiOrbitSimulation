#%  - - - - - -
# %   i a u R z
# %  - - - - - -
# %
# %  Rotate an r-matrix about the z-axis.
# %
# %  This function is part of the International Astronomical Union's
# %  SOFA (Standards Of Fundamental Astronomy) software collection.
# %
# %  Status:  vector/matrix support function.
# %
# %  Given:
# %     psi              angle (radians)
# %
# %  Given and returned:
# %     r                r-matrix, rotated
# %
# %  Notes:
# %
# %  1) Calling this function with positive psi incorporates in the
# %     supplied r-matrix r an additional rotation, about the z-axis,
# %     anticlockwise as seen looking towards the origin from positive z.
# %
# %  2) The additional rotation can be represented by this matrix:
# %
# %         (  + cos(psi)   + sin(psi)     0  )
# %         (                                 )
# %         (  - sin(psi)   + cos(psi)     0  )
# %         (                                 )
# %         (       0            0         1  )
# %
# %  This revision:  2012 April 3
# %
# %  SOFA release 2012-03-01
# %
from math import sin,cos

def iauRz(psi, r):

    s = sin(psi)
    c = cos(psi)

    a00 =   c*r[0,0] + s*r[1,0]
    a01 =   c*r[0,1] + s*r[1,1]
    a02 =   c*r[0,2] + s*r[1,2]
    a10 = - s*r[0,0] + c*r[1,0]
    a11 = - s*r[0,1] + c*r[1,1]
    a12 = - s*r[0,2] + c*r[1,2]

    r[0,0] = a00
    r[0,1] = a01
    r[0,2] = a02
    r[1,0] = a10
    r[1,1]= a11
    r[1,2] = a12

    return r

def test():
    from numpy import zeros
    from iauIr import iauIr
    from math import pi
    rpom = zeros([3, 3])
    rpom = iauIr(rpom)
    psi= pi/6
    r=iauRz(psi, rpom)
    print('r',r)


if __name__ == "__main__":

    test()