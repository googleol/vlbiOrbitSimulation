
from OrbitElementsToRV import orbit_element_to_rv
from numpy import array,sqrt,arccos,pi
from ephemeris_position_ECRF import ephemeris_sun_lunar_ECRF
from math import degrees

def Visibility_for_celestial_body (direction_vector,r,time):
    '''
  
  :param direction_vector: 需要观测天区方向矢量，在ICRF地心坐标系下，严格来说是ECRF
  :param r: 卫星位置，在ECRF坐标系下，
  :param time:当前儒略日
  :return: 可观测时间段

    '''
    R_earth=6378.137 #km
    R_sun=696000 #km
    R_moon=1738 #km
    r=r/1000  #m化成km
    Distance_sat_EarthCenter=sqrt(r.dot(r))

    Position_satellite_ECRF=r

    # 获得太阳和月亮在ECRF下的坐标
    Position_sun_ECRF, Position_moon_ECRF = ephemeris_sun_lunar_ECRF(time)
    vector_target=direction_vector #卫星指向目标天区的方向矢量



    #卫星——目标天区矢量和卫星——地心矢量夹角

    x = Position_satellite_ECRF*(-1) #化为指向地心的矢量
    y =  vector_target#卫星指向目标天区的矢量
    # 两个向量
    Lx = sqrt(x.dot(x))
    Ly = sqrt(y.dot(y))
    # 相当于勾股定理，求得斜线的长度
    cos_angle = x.dot(y) / (Lx * Ly)
    # 求得cos_sita的值再反过来计算，绝对长度乘以cos角度为矢量长度，初中知识。。
    angle_arc = arccos(cos_angle)
    angle_degree_earth_target = degrees(angle_arc)
    # 变为角度


    #切线长度
    #切线与卫星——地心矢量角度，即地球所占角度

    l=sqrt(R_earth**2+Distance_sat_EarthCenter**2)


    cos_angle= Distance_sat_EarthCenter/l


    angle_arc = arccos(cos_angle)
    angle_degree_earth_occupied = degrees(angle_arc)
    # 变为角度



    #判断地球是否挡住了卫星的观测天区
    if angle_degree_earth_target >= angle_degree_earth_occupied :


        Visibility_earth_target=1


    else :

        Visibility_earth_target=0










    # 卫星——目标天区矢量和卫星——日心矢量夹角

    x = Position_satellite_ECRF * (-1) +Position_sun_ECRF # 化为指向日心的矢量
    y = vector_target  # 卫星指向目标天区的矢量
    # 两个向量
    Lx = sqrt(x.dot(x))
    Ly = sqrt(y.dot(y))
    # 相当于勾股定理，求得斜线的长度
    cos_angle = x.dot(y) / (Lx * Ly)
    # 求得cos_sita的值再反过来计算，绝对长度乘以cos角度为矢量长度，初中知识。。
    angle_arc = arccos(cos_angle)
    angle_degree_sun_target = degrees(angle_arc)
    # 变为角度



    # 切线长度
    # 切线与卫星——日心矢量角度，即太阳所占角度
    Vector_sat_sunCenter=Position_satellite_ECRF * (-1) +Position_sun_ECRF
    Distance_sat_sunCenter = sqrt(Vector_sat_sunCenter.dot(Vector_sat_sunCenter))
    l = sqrt(R_sun ** 2 + Distance_sat_sunCenter ** 2)

    cos_angle = Distance_sat_sunCenter / l

    angle_arc = arccos(cos_angle)
    angle_degree_sun_occupied = degrees(angle_arc)
    # 变为角度

    # 判断太阳是否挡住了卫星的观测天区
    if angle_degree_sun_target >= angle_degree_sun_occupied:

        Visibility_sun_target = 1


    else:

        Visibility_sun_target = 0





    # 卫星——目标天区矢量和卫星——月心矢量夹角

    x = Position_satellite_ECRF * (-1) + Position_moon_ECRF # 化为指向月心的矢量
    y = vector_target  # 卫星指向目标天区的矢量
    # 两个向量
    Lx = sqrt(x.dot(x))
    Ly = sqrt(y.dot(y))
    # 相当于勾股定理，求得斜线的长度
    cos_angle = x.dot(y) / (Lx * Ly)
    # 求得cos_sita的值再反过来计算，绝对长度乘以cos角度为矢量长度，初中知识。
    angle_arc = arccos(cos_angle)
    angle_degree_moon_target = degrees(angle_arc)
    # 变为角度



    # 切线长度
    # 切线与卫星——月心矢量角度，即月亮所占角度
    Vector_sat_moonCenter= Position_satellite_ECRF * (-1) + Position_moon_ECRF
    Distance_sat_moonCenter=sqrt(Vector_sat_moonCenter.dot(Vector_sat_moonCenter))
    l = sqrt(R_moon ** 2 + Distance_sat_moonCenter ** 2)

    cos_angle = Distance_sat_moonCenter / l

    angle_arc = arccos(cos_angle)
    angle_degree_moon_occupied = degrees(angle_arc)
    # 变为角度

    # 判断月亮是否挡住了卫星的观测天区
    if angle_degree_moon_target >= angle_degree_moon_occupied:

        Visibility_moon_target = 1


    else:

        Visibility_moon_target= 0

    if 0 in (Visibility_moon_target, Visibility_earth_target, Visibility_sun_target):

        Visibility_result=0

    else:

        Visibility_result=1


    return Visibility_result



def test():

    r=array([3e6,4e6,4e6])
    time=2444395.7
    direction_vector=array([1,1,1])
    Visibility=Visibility_for_celestial_body(direction_vector,r, time)
    print(Visibility)



if __name__ == "__main__":

    test()



