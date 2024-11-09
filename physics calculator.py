# Physics Calculator
# Elastic Collision


for i in range(int(input("how many questions are there "))):
    print("Put 1 if the problem is a change in momentum ")
    print(">>>")
    print("Put 2 if the problem is an explosion ")
    print(">>>")
    print("Put 3 if the problem is an inelastic collision")
    print(">>>")
    print("Put 4 if the problem is an elastic collision")
    print(">>>")

    pD = int(input("Number Problem: "))

    if(pD == 1):
        def changeMomen(m, vi, vf):
            t7 = m * vi
            t8 = m * vf
            print("Answer: " + str(t8 - t7))
        m1 = int(input("What is the mass of the object "))
        vi1 = int(input("What is the initial velocity of the object "))
        vf1 = int(input("What is the final velocity of the object "))
        changeMomen(m1, vi1, vf1)

    elif(pD == 2):
        mtotal = int(input("What is the original mass of the object "))
        mtotalv = int(input("What is the original objects velocity "))
        m1 = int(input("What is the mass of the first sub piece "))
        v1 = int(input("What is the velocity of the first sub piece "))
        m2 = int(input("What is the mass of the second sub piece "))
        sum3 = mtotal * mtotalv
        sum4 = m1 * v1
        sum5 = sum3 + sum4
        sum6 = sum5 / m2
        print("Asnwer: " + str(sum6))

    elif(pD == 3):
        m1 = float(input("What is the mass of the first object "))
        v1i = float(input("What is the initial velocity of the first object "))
        v1f = float(input("What is the final velocity of the first object "))
        m2 = float(input("What is the mass of the second object "))
        v2i = float(input("What is the initial velocity of the second object "))
        answer1 = m1 * v1i + m2 * v2i
        answer2 = m1 * v1f
        answer3 = answer1 - answer2
        answer4 = answer3 / m2
        print("Final Velocity of the Second Object: " + str(answer4))

    elif(pD == 4):
        m1 = float(input("What is the mass of the first object "))
        v1i = float(input("What is the initial velocity of the first object "))
        v1f = float(input("What is the final velocity of the first object "))
        m2 = float(input("What is the mass of the second object "))
        v2i = float(input("What is the initial velocity of the second object"))
        sum1 = m1 * v1i + m2 * v2i
        sum2 = m1 * v1f
        sum3 = sum1 - sum2
        sum4 = sum3 / m2
        print("Answer: " + str(sum4))




