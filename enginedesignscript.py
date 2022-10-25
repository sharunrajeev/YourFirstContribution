# jn snw
def int_input(string):
    temp = input(string)
    try:
        return int(temp)
    except:
        return float(temp)


def str_parse(page, table):
    return "- Design Data(I.C)(Page " + str(page) + ", Table " + str(
        table) + ")"


def std_dim(num):
    for i in [
            30, 32, 36, 38, 40, 42, 45, 50, 52, 56, 58, 60, 63, 68, 70, 75, 80,
            85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 140, 145, 150, 160,
            170, 180, 190, 200, 210
    ]:
        if i >= num:
            return i


def title_print(text):
    print(
        "\n------------------------------------------------------------------------------------------------------------\n"
    )
    print(text)
    print(
        "\n------------------------------------------------------------------------------------------------------------\n"
    )


def thread_selection(ac):
    threads = [
        1, 1.2, 1.4, 1.6, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0,
        14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 27.0, 30.0, 33.0, 36.0, 39.0, 42.0,
        45.0, 48.0
    ]
    area = [
        0.41, 0.66, 0.98, 1.58, 2.13, 4.94, 8.53, 14.5, 19.21, 27.75, 34.14,
        45.28, 57.99, 76.81, 111.0, 152.0, 188.0, 251.0, 311.0, 353.0, 459.0,
        580.0, 716.0, 813.0, 950.0, 1121.0, 1306.0, 1505.0
    ]
    for i, j in enumerate(area):
        if j >= ac:
            return threads[i], j
    return threads[-1], area[-1]


transcript = " "


def display(*args):
    global transcript
    temp = str(" ".join([str(i) for i in args]))
    transcript += temp + "\n"
    print(temp)


title_print("Data Acquisition")
display(
    "Instructions:\n1) Fill in the problem description as specified\n2) Enter '0' if details not mentioned"
)
fuel_type = input("\nEnter Fuel Type:\t\t").lower()
number_of_strokes = int_input("Enter Number of Strokes:\t")
brake_power = int_input("Enter Brake Power (in kw):\t")
operating_speed = int_input("Enter Operating Speed(in rpm):\t")
overspeed = int_input("Enter Overspeed(in rpm) \t")
compression_ratio = int_input("Enter Compression Ratio:\t")

title_print("Determination of bore and stroke of the Engine")
display("\nStep 1:\t Assumptions\n")

#compression ratio if not provided is 14, 7 for petrol and diesel engine respectively
#compression ratio is not mentioned if it isn't provided
if compression_ratio == 0:
    if fuel_type == "diesel":
        compression_ratio = 14
        display("\tCompression Ratio(Rc) = 14\t\t\t" + str_parse(5, 3.1))
    else:
        compression_ratio = 7

#mechanical efficiency
n_mech = 0
if fuel_type == "petrol":

    n_mech = 0.8
else:
    if number_of_strokes == 2:
        n_mech = 0.75
    else:
        n_mech = 0.8

display("\tMechanical Efficiency :" + str(n_mech) + "\t\t\t" +
        str_parse(6, 3.5))

p_mi = 0
if fuel_type == "diesel":
    p_mi = 0.9
    display("\tMean Indicated Pressure P_mi = 0.9 N/mm2\t\t" +
            str_parse(5, 3.2))
else:
    p_mi = 1
    display("\tMean Indicated Pressure P_mi = 1 N/mm2\t\t" + str_parse(5, 3.2))

l_d_ratio = 0
if fuel_type == "petrol":
    l_d_ratio = 0.85
else:
    l_d_ratio = 1
display("\tL/D=1\t\t\t\t\t\t" + str_parse(6, 3.7))

display("\tMaximum Pressure p_max=p_mi*R^r\t\t\t" + str_parse(7, 3.9))

###############################################################

display("\nStep 2:\t To calculate Maximum Pressure\n")
p_max = round(p_mi * (compression_ratio**1.4), 4)
display("\tp_max = p_mi*R^r = " + str(p_max) + " = " + str(round(p_max, 1)) +
        " bar\t\t" + str_parse(7, 3.9))
p_max = round(p_max, 1)

#################################################################
display("\nStep 3:\t To calculate the bore and stroke of engine\n")
display("\tMechanical Efficiency n_mech = B.P./I.P\t\t" + str_parse(7, 3.9))
display("\t\t" + str(n_mech) + " = " + str(brake_power) + " / I.P")

i_p = round(brake_power / n_mech, 2)

display("\t\tI.P =", i_p)
display("\tI.P = (p_mi*L*A*n)/60")
display("\t\tI.P =", i_p)
display("\t\tp_mi =", p_mi)
nos = 0
if overspeed == 0:
    nos = round(2 * operating_speed / number_of_strokes, 2)
    display("\t\tNumber of Strokes n =" + str(operating_speed) + "/",
            number_of_strokes / 2, "=", nos)
else:
    nos = round(2 * overspeed / number_of_strokes, 2)
    display("\t\tNumber of Strokes n =", overspeed, "/", number_of_strokes / 2,
            "=", nos)
display("\t Solving the equations...")

D = round(((4 * i_p * (10**3) * 60) / (l_d_ratio * 3.142 * p_mi *
                                       (10**6) * nos))**0.3333, 4)

display("\tD =", D, "m ==", round(D * 1000), "mm")

L = round(D * l_d_ratio, 4)
display("\tL =", round(L * 1000), "mm")
display(
    "\tFrom I.C engine design data book,\n\t\t selecting standard values\t\t" +
    str_parse(6, 3.6))

L = std_dim(L * 1000)
D = std_dim(D * 1000)
display("\tCylinder Bore D =", D, "mm")
display("\tStroke L =", L, "mm")
##################################################################################
title_print("2. Design of cylinder head and wet liner")
display("\nStep 4:\t To find the minimum thickness of liner\n")
t_min = 0
s_d = 90
display(
    "\tA) t_min=D(((s_d+0.4*p_max)/(s_d-1.3*p_max))**0.5-1)/2\n\t\t\t\t\t\t\t"
    + str_parse(12, 4.5))
display("\t\ts_d - Design Stress = 90 Mpa")
display("\t\tp_max =", p_max, "bar")
t_min = round(
    D * (((s_d + 0.4 * p_max * 0.1) / (s_d - 1.3 * p_max * 0.1))**0.5 - 1) / 2,
    2)
display("\t\tt_min=", t_min)
display("\tB)By Empirical Relation, t=D/15")
display("\t\tt_min=", round(D / 15, 2), "=", round(D / 15))
display("\tSelecting higher of two values, t=", max(t_min, round(D / 15)),
        "mm")
t_min = max(t_min, round(D / 15))
##########################################
display("\nStep 5:\t To find the pressure stress induced\n")
display("\tSx=p_max*D/2*t")
s_x = round((p_max * 0.1 * D) / (2 * t_min), 2)
display("\tSx=", s_x, "N/mm2")
###############################
display("\nStep 6:\t To find the thermal stress induced\n")

display("\tSt=(e*alpha*delta_t)/(2*(1-mu))\t\t\t" + str_parse(12, 4.5))
display("\t\tE=20.6*10^4 Mpa, mu=0.3, alpha= 11.1*10^6")
display("\t\tdelta_t=100 degree celcius")
s_t = round((20.6 * (10**4) * 11.1 * (10**(-6)) * 100) / (2 * (1 - 0.3)), 2)
display("\tSt=", s_t, "Nmm2")
####################################
display("\nStep 7:\t To find the total stress induced in the material\n")
S_T = s_t + s_x
S_T = round(S_T, 2)
display("\tS_T = s_t+s_x =", S_T, "Nmm2")
if S_T > 200:
    display("\nAs", S_T, "Nmm2 >200 Nmm2, Design is unsafe")
else:
    display("\nAs", S_T, "Nmm2 <200 Nmm2, Design is safe")

title_print("3. Design of stud")

display("\nStep 8:\t To find maximum gas force\t\t\t" + str_parse(19, 4.10) +
        "\n")

display("\tF_g=p_max*pi*D^2/4")
F_g = round((p_max * (10**5) * 3.1428 * ((D / 1000)**2)) / 4000, 2)
display("\tF_g = ", str(F_g), "KN\n")
F_max = round(F_g * 1000 / 4, 2)

display("\tF_max = Fg/ng")
display("\t\tng = number of studs = 4")
display("\tF_max = ", str(F_max), "N")

display("\nStep 9:\t To find preloading force of stud\n")

display("\tF_pl = m*(1-x)F_max")
display("\t\tm = Stud tightening coefficient = 1.75\t\t...without gasket")
display("\t\tx = Coefficient of main load of threaded joint = 0.2")
F_pl = round(F_g * 1000 * (1 - 0.2) * 1.75 / 1000, 2)
display("\tF_pl = ", str(F_pl), "kN")

display("\nStep 10: To find total load on stud\n")
display("\tFt = x*F_max+F_pl")
F_t = round(((0.2 * F_max) + (1000 * F_pl)) / 1000, 2)
display("\tFt =", F_t, "kN")

display("\nStep 11: To find diameter of stud\n")
display("\tSd = Ft/Ac")
display("\t\tSd = Design stress in stud = 145 Mpa (SAE 2330)")
A_c = round(F_t * 1000 / 145, 2)
display("\tAc =", A_c, "mm2")
text, area = thread_selection(A_c)
display("\tSelecting bolts of M", str(text), "with Ac =", area,
        "\t" + str_parse(17, 4.9))

title_print("4. Design of Piston")
display("\nStep 12: To select piston material\n")
display("\tFor minimum inertia forces let us,\t\t" + str_parse(8, 4.1))
display("\tAllowable stress S_d = 70 Mpa")
S_d = 70
display("\nStep 13: To find the crown thickness\n")
display("\tA) Maximum pressure criteria")
t_c1 = round((((3 * p_max * 0.1) / (16 * 70))**0.5) * D, 2)
display("\ttc =", t_c1, "mm")
display("\tB) Thermal stress criteria")
display("\ttc=q*D^2*10*-2/16*C1*T")
display("\t\tC1 = Heat Conduction Factor = 1.986 Kj/cm-hr C")
display(
    "\t\tT = Temperature difference between centre and edge of piston head = 75 C"
)
display("\t\tq = Heat Flux flowing through crown")
display("\t\tq = K*BSFC*CV*Pb/A*nc")
display("\t\t\tK = 0.08")
display("\t\t\tCV = 43000 KJ/kg")
display("\t\t\tpb = Brake Power =", brake_power)
a_piston = round((3.1428 * ((D / 10)**2)) / 4, 2)
display("\t\t\tA =  Area of Piston = pi*D^2/4 =", a_piston)
display("\t\t\tnc = Number of cylinders = 1")
display("\t\t\tBSFC = 0.266")
q = round(0.08 * 0.266 * 43000 * (brake_power / (a_piston)), 2)
display("\t\tq= ", q)
t_c2 = round(10 * ((D**2) * q * (10**-2)) / (16 * 1.986 * 75), 2)
display("\t\tt_c =", t_c2)
if max(t_c1, t_c2) < 100:
    display("\tSelecting higher of the two values")
    display("\tt_c =", round(max(t_c1, t_c2)))
else:
    display("\tSelecting practical value, tc = 40mm")

display("\nStep 14: To find radial thickness of piston ring\t" +
        str_parse(9, 4.2) + "\n")
display("\tUsing empirical relationship(for compression ring)")
display("\tT_r = (0.04 - 0.045) D")
t_r = 0.042 * D
display("\tT_r =", t_r, " = ", round(t_r), "mm")
t_r = round(t_r)

display("\nStep 15: To find the number of piston rings\t\t" +
        str_parse(9, 4.2))
display("\tn = 0.4 * (D)^0.5")

display("\tn =", round(0.4 * (D**0.5), 2), " = ", round(0.4 * (D**0.5)))
n = round(0.4 * (D**0.5))

display("\nStep 16: To find axial thickness of piston rings\t" +
        str_parse(9, 4.2) + "\n")
display("\tUsing empirical relationship")
t_am = round(0.8 * t_r, 2)
display("\tt_am = 0.8*t_r =", t_am)

display("\nStep 17: To find other dimensions\n")
display("\tGap between free ends G1 = 3.8 t_r =", round(3.8 * t_r, 2), "mm")
display("\tGap between ring ends when ring is in the cylinder = 0.003 D =",
        round(0.003 * D, 2), "mm")
display("\tThickness between ring grooves(land) = 0.085 t_a =",
        round(0.85 * t_am, 2), "mm")

title_print("5. Design of connecting rod")

display("\nStep 18: To calculate maximum gas force\n")
display("\tF_g =", F_g, "kN")

display("\nStep 19: To find the inertia force\t\t" + str_parse(19, 4.10) +
        "\n")
display("\tFr=We*w^2*r_c*(1+1/n)")
display("\n\tWe = Effective mass (kg) = W1 + W2 + W3")
display("\n\tW1 = Mass of piston")
W1 = round(200 * (3.142 / 4) * ((D / 1000)**2), 2)
display("\tW1 =", W1, "kg")
display("\n\tW2 = Mass of connecting rod")
W2 = round(300 * (3.142 / 4) * ((D / 1000)**2), 2)
display("\tW2 =", W2, "kg")
display("\n\tW3 = Unbalanced parts of crank shaft")
W3 = round(300 * (3.142 / 4) * ((D / 1000)**2), 2)
display("\tW3 =", W3, "kg")
display("\tEffective mass We =", W1 + W2 + W3, "kg")
display("\tCrank Radius = L/2 =", round(D / 2000, 2))
display("\tAngular Speed = 2*pi*N/60 =",
        round(2 * 3.142 * operating_speed / 60, 2), "rad/sec")
display("\tObliquity Ratio n = 4\t\t\t\t...Assume\n")
F_i = round(((W1 + W2 + W3) * ((2 * 3.142 * operating_speed / 60)**2) *
             (D / 2000) * (1 + (1 / 4))) / 1000, 2)
display("\tF_i =", F_i, "kN")

display("\nStep 20: To find normal load acting on connecting rod\n")
F_n = abs(F_g - F_i)
display("\tFn = F_g - F_i =", F_n, "kN")

display("\nStep 20: To find the thickness of section\n")
t = round(10 * ((F_n / 8.8)**0.5), 2)
display("\tt =", t, "mm")