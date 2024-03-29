import cmath

def padZeroes(data):
    # if already power of 2 then return
    if len(data) & (len(data) - 1) == 0:
        return data
    nearestPowerOf2 = 2 ** (len(data) - 1).bit_length()
    return data + [0] * (nearestPowerOf2 - len(data))

def FFT(P, omega):
    n = len(P)
    if n == 1:
        return P
    Pevens = P[::2]
    Podds = P[1::2]

    yevens = FFT(Pevens, omega)
    yodds = FFT(Podds, omega)

    y = [0] * n

    for k in range(n // 2):
        t = omega ** k
        y[k] = yevens[k] + (t * yodds[k])
        y[k + n // 2] = yevens[k] - (t * yodds[k])

    return y

data = [1, 2, -4j, 3j]
# before running, pad zeroes to make power of 2
data = padZeroes(data)

# FORWARD: omega = e^(-2i*pi/n)
forwardOmega = cmath.exp(-2j * cmath.pi / len(data))
forwardResult = FFT(data, forwardOmega)
print(f"forward: {forwardResult}")

# INVERSE: omega = e^(2i*pi/n)
inverseOmega = cmath.exp(2j * cmath.pi / len(data))
inverseResult = [x/len(forwardResult) for x in FFT(forwardResult, inverseOmega)]
print(f"inverse of forward: {inverseResult}")
