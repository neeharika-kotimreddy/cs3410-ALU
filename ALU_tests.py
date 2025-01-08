import random


def left_shift_tests():
    f = open("left_shift_tests.txt", "w")
    f.write('B[32] ' + 'Cin[1] ' +
            'Sa[5] ' + 'C[32] ' + '\n')
    f.write("#Random cases start here")
    for i in range(0, 25):
        B = random.randint(-2147483647, 2147483647)
        Cin = 0
        Sa = random.randint(0, 31)
        C = B << Sa
        f.write(str(B) + " " + str(Cin) + " " +
                str(Sa) + " " + str(C) + '\n')

    edges = [0, 1, -1, -2147483648, 2147483647]
    f.write("#edge cases start here")
    for i in range(0, 10):
        for j in range(0, 10):
            B = random.choice(edges)
            Cin = 0
            Sa = random.randint(0, 31)
            C = B << Sa
            f.write(str(B) + " " + str(Cin) + " " +
                    str(Sa) + " " + str(C) + '\n')


def adder_tests():
    f = open("adder_tests.txt", "w")
    f.write('A[32] ' + 'B[32] ' + 'Cin[1] ' + 'C[32] ' + 'V[1] ' + '\n')
    f.write("#Random cases start here" + '\n')
    for i in range(0, 25):
        A = random.randint(-2147483647, 2147483647)
        B = random.randint(-2147483647, 2147483647)
        Cin = random.choice([0, 1])
        if Cin == 1:
            C = A-B
        else:
            C = A+B
        if (C < -2147483647 or C > 2147483647):
            V = 1
        else:
            V = 0
        f.write(str(A) + " " + str(B) + " " + str(Cin) +
                " " + str(C) + " " + str(V) + '\n')

    edges = [0, 1, -1, -2147483648, 2147483647]
    f.write("#edge cases start here" + '\n')
    for i in range(0, 10):
        for j in range(0, 10):
            A = random.choice(edges)
            B = random.choice(edges)
            Cin = random.choice([0, 1])
            if Cin == 1:
                C = A-B
            else:
                C = A+B

            if (C < -2147483648 or C > 2147483647):
                V = 1
            else:
                V = 0
            f.write(str(A) + " " + str(B) + " " + str(Cin) +
                    " " + str(C) + " " + str(V) + '\n')


def rshift(val, n): return (val % 0x100000000) >> n


def alu_tests():
    f = open("ALU_test_cases.txt", "w")
    # A[32] B[32] Op[4] Sa[5] = C[32] V
    f.write("#Random cases start here" + '\n')
    f.write('A[32] ' + 'B[32] ' + 'Op[4] ' +
            'Sa[5] ' + 'C[32] ' + 'V[1] ' + '\n')
    # tests for AND 0101 opcode: 5
    for i in range(0, 25):
        A = random.randint(-2147483647, 2147483647)
        B = random.randint(-2147483647, 2147483647)
        Op = 5
        Sa = 0
        C = int(A & B)
        V = 0
        f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                str(Sa) + " " + str(C) + " " + str(V) + '\n')

    # tests for OR 0100 opcode: 4
    for i in range(0, 25):
        A = random.randint(-2147483647, 2147483647)
        B = random.randint(-2147483647, 2147483647)
        Op = 4
        Sa = 0
        C = int(A | B)
        V = 0
        f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                str(Sa) + " " + str(C) + " " + str(V) + '\n')

    # tests for xor 0010 opcode: 2
    for i in range(0, 25):
        A = random.randint(-2147483647, 2147483647)
        B = random.randint(-2147483647, 2147483647)
        Op = 2
        Sa = 0
        C = A ^ B
        V = 0
        f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                str(Sa) + " " + str(C) + " " + str(V) + '\n')

    # tests for nor 0011 opcode: 3
    for i in range(0, 25):
        A = random.randint(-2147483647, 2147483647)
        B = random.randint(-2147483647, 2147483647)
        Op = 3
        Sa = 0
        C = int(~(A | B))
        V = 0
        f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                str(Sa) + " " + str(C) + " " + str(V) + '\n')

    # tests for shift right logical 1100 opcode: 12
    for i in range(0, 25):
        A = 0
        B = random.randint(-2147483647, 2147483647)
        Op = 12
        Sa = random.randint(0, 31)
        C = rshift(B, Sa)
        #C = numpy.right_shift(B, Sa)
        V = 0
        f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                str(Sa) + " " + str(int(C)) + " " + str(V) + '\n')

    # tests for shift right arithmetic 1101 opcode: 13
    for i in range(0, 25):
        A = 0
        B = random.randint(-2147483647, 2147483647)
        Op = 13
        Sa = random.randint(0, 31)
        C = B >> Sa
        V = 0
        f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                str(Sa) + " " + str(C) + " " + str(V) + '\n')

    # tests for not equal 0000 opcode: 0
    for i in range(0, 25):
        A = random.randint(-2147483647, 2147483647)
        B = random.randint(-2147483647, 2147483647)
        Op = 0
        Sa = 0
        C = int(A != B)
        V = 0
        f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                str(Sa) + " " + str(C) + " " + str(V) + '\n')

    # tests for equal 0001 opcode: 1
    for i in range(0, 25):
        A = random.randint(-2147483647, 2147483647)
        B = random.randint(-2147483647, 2147483647)
        Op = 1
        Sa = 0
        C = int(A == B)
        V = 0
        f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                str(Sa) + " " + str(C) + " " + str(V) + '\n')

    # tests for le 1110 opcode: 14
    for i in range(0, 25):
        A = random.randint(-2147483647, 2147483647)
        B = 0
        Op = 14
        Sa = 0
        C = int(A <= 0)
        V = 0
        f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                str(Sa) + " " + str(C) + " " + str(V) + '\n')

    # tests for gt 1111 opcode: 15
    for i in range(0, 25):
        A = random.randint(-2147483647, 2147483647)
        B = 0
        Op = 15
        Sa = 0
        C = int(A > 0)
        V = 0
        f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                str(Sa) + " " + str(C) + " " + str(V) + '\n')
    # tests for subtract 101x opcode: 10 and 11
    for i in range(0, 25):
        A = random.randint(-2147483647, 2147483647)
        B = random.randint(-2147483647, 2147483647)
        Op = random.choice([10, 11])
        Sa = 0
        C = A - B

        if (C < -2147483647 or C > 2147483647):
            V = 1
        else:
            V = 0

        f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                str(Sa) + " " + str(C) + " " + str(V) + '\n')

    edges = [0, 1, -1, -2147483648, 2147483647]

    # EDGE CASES
    f.write("#edge cases start here" + '\n')

    # tests for AND 0101 opcode: 5
    for i in range(0, 10):
        for j in range(0, 10):
            A = random.choice(edges)
            B = random.choice(edges)
            Op = 5
            Sa = 0
            C = int(A & B)
            V = 0
            f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                    str(Sa) + " " + str(C) + " " + str(V) + '\n')

    # tests for OR 0100 opcode: 4
    for i in range(0, 10):
        for j in range(0, 10):
            A = random.choice(edges)
            B = random.choice(edges)
            Op = 4
            Sa = 0
            C = int(A | B)
            V = 0
            f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                    str(Sa) + " " + str(C) + " " + str(V) + '\n')

    # tests for xor 0010 opcode: 2
    for i in range(0, 10):
        for j in range(0, 10):
            A = random.choice(edges)
            B = random.choice(edges)
            Op = 2
            Sa = 0
            C = A ^ B
            V = 0
            f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                    str(Sa) + " " + str(C) + " " + str(V) + '\n')

    # tests for nor 0011 opcode: 3
    for i in range(0, 10):
        for j in range(0, 10):
            A = random.choice(edges)
            B = random.choice(edges)
            Op = 3
            Sa = 0
            C = int(~(A | B))
            V = 0
            f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                    str(Sa) + " " + str(C) + " " + str(V) + '\n')

    # tests for shift right logical 1100 opcode: 12
    for i in range(0, 10):
        for j in range(0, 10):
            A = 0
            B = random.choice(edges)
            Op = 12
            Sa = random.randint(0, 31)
            C = rshift(B, Sa)
            #C = numpy.right_shift(B, Sa)
            V = 0
            f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                    str(Sa) + " " + str(int(C)) + " " + str(V) + '\n')

    # tests for shift right arithmetic 1101 opcode: 13
    for i in range(0, 10):
        for j in range(0, 10):
            A = 0
            B = random.choice(edges)
            Op = 13
            Sa = random.randint(0, 31)
            C = B >> Sa
            V = 0
            f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                    str(Sa) + " " + str(C) + " " + str(V) + '\n')

    # tests for not equal 0000 opcode: 0
    for i in range(0, 10):
        for j in range(0, 10):
            A = random.choice(edges)
            B = random.choice(edges)
            Op = 0
            Sa = 0
            C = int(A != B)
            V = 0
            f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                    str(Sa) + " " + str(C) + " " + str(V) + '\n')

    # tests for equal 0001 opcode: 1
    for i in range(0, 10):
        for j in range(0, 10):
            A = random.choice(edges)
            B = random.choice(edges)
            Op = 1
            Sa = 0
            C = int(A == B)
            V = 0
            f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                    str(Sa) + " " + str(C) + " " + str(V) + '\n')

    # tests for le 1110 opcode: 14
    for i in range(0, 10):
        for j in range(0, 10):
            A = random.choice(edges)
            B = 0
            Op = 14
            Sa = 0
            C = int(A <= 0)
            V = 0
            f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                    str(Sa) + " " + str(C) + " " + str(V) + '\n')

    # tests for gt 1111 opcode: 15
    for i in range(0, 10):
        for j in range(0, 10):
            A = random.choice(edges)
            B = 0
            Op = 15
            Sa = 0
            C = int(A > 0)
            V = 0
            f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                    str(Sa) + " " + str(C) + " " + str(V) + '\n')
    # tests for subtract 101x opcode: 10 and 11
    for i in range(0, 10):
        for j in range(0, 10):
            A = random.choice(edges)
            B = random.choice(edges)
            Op = random.choice([10, 11])
            Sa = 0
            C = A - B

            if (C < -2147483648 or C > 2147483647):
                V = 1
            else:
                V = 0

            f.write(str(A) + " " + str(B) + " " + str(Op) + " " +
                    str(Sa) + " " + str(C) + " " + str(V) + '\n')


left_shift_tests()
print("done with left tests")
adder_tests()
print("done with add tests")
alu_tests()
print("done with alu tests")
