#2018/12/13与matlab程序对比，没有计算错误
import numpy as np
import math


def rv_to_orbit_element (R,V):
    '''
    :param r km ,velocity km/s
    :return: orbit_element: semi_major_axis km, Eccentricity,
           Inclination, RAAN, Perigee, True_Anomaly
           半长轴输出单位为km,其余角度输出单位为角度

    '''
    mu = 398600
    H_vector = np.cross(R,V)
    h = np.sqrt(H_vector.dot(H_vector))
    r = np.sqrt(R.dot(R))
    v = np.sqrt(V.dot(V))
    vr = (R.dot(V))/r
    Eccentricity_vector = 1/mu*((v**2-mu/r)*R-r*vr*V)
    Eccentricity = np.sqrt(Eccentricity_vector.dot(Eccentricity_vector))
    semi_major_axis = h**2/mu/(1 - Eccentricity**2)
    Inclination = np.arccos(H_vector[2]/h)

    #Calculate the node line N

    N = np.cross([0,0,1],H_vector)
    n = np.sqrt(N.dot(N))
    eps = 1.e-9

    #Calculate the right ascension the ascending node(RAAN)

    if n != 0:  # 判断是否为赤道面平行轨道
        RAAN = np.arccos(N[0]/n)

        if N[1] < 0:

            RAAN = 2*math.pi - RAAN

    else:

        RAAN = np.nan

    #Calculate the argument of perigee

    if n != 0:
        if Eccentricity > eps:

            Perigee = np.arccos((N.dot(Eccentricity_vector))/n/Eccentricity)

            if Eccentricity_vector[2] < 0:

               Perigee = 2*math.pi - Perigee

        else:

            Perigee = np.nan

    else:

        Perigee = np.nan

    #Calculate the true anomaly

    if Eccentricity > eps:

        TA = np.arccos((Eccentricity_vector.dot(R))/Eccentricity/r)

        if vr < 0:

            TA = 2*math.pi - TA
    else:

        TA=np.nan

    Inclination=math.degrees(Inclination)
    RAAN=math.degrees(RAAN)
    Perigee=math.degrees(Perigee)
    True_anomaly=math.degrees(TA)

    return np.array([semi_major_axis,Eccentricity,Inclination,RAAN,Perigee,True_anomaly])

def test():
    R=np.array([4.86711880e+03,  2.77837913e+03,  3.33434849e+02])
    V=np.array([-4.35455694e+00,  7.98629140e+00,  1.52013651e+00])
    b=rv_to_orbit_element(R,V)
    print(b)



if __name__ == "__main__":

    test()
