import numpy as np
import matplotlib.pyplot as plt
def hz_2_oct(frequencies):
    return np.log2((frequencies)/(440// 16))


def chroma_filter(sr,n_fft):

    wts = np.zeros((12, n_fft))

    print "intinalized=\n",wts

    frequencies = np.linspace(0, sr, n_fft, endpoint=False)[1:]
    print "frequencies=\n",frequencies
    frqbins = 12* hz_2_oct(frequencies)
    print "frequencybins=\n",frqbins

    frqbins = np.concatenate(([frqbins[0] - 1.5 * 12], frqbins))

    binwidthbins = np.concatenate((np.maximum(frqbins[1:] - frqbins[:-1],
                                              1.0), [1]))
    print "binwidthbins=\n",binwidthbins
    D = np.subtract.outer(frqbins, np.arange(0,12, dtype='d')).T
    print "D=\n",D
    n_chroma2 = np.round(float(12) / 2)

    print "n_chroma2=",n_chroma2
    D = np.remainder(D + n_chroma2 + 10 *12,12) - n_chroma2

    print "D after raminder =\n",D
    wts = np.exp(-0.5 * (2 * D / np.tile(binwidthbins, (12, 1))) ** 2)

    print "wts=\n",wts

    wts *= np.tile(
        np.exp(-0.5 * (((frqbins / 12 - 5) /2) ** 2)),
        (12, 1))


    wts = np.roll(wts, -3, axis=0)


    return np.ascontiguousarray(wts[:, :int(1 + n_fft / 2)]),D


sr=44100
n_fft=4096
F,D=chroma_filter(sr,n_fft)
plt.figure(1)
plt.plot(F.T)
plt.figure(2)
plt.scatter(np.arange(4096),D[0][:])
plt.show()