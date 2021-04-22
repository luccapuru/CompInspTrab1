import matplotlib.pyplot as plt
import matplotlib

taxaCross = [0.3, 0.6, 0.9]
taxaMutacao = [0.02, 0.04, 0.08]
convergencia = [26.16, 24.005, 23.583333333333332, 23.0725, 22.098, 21.69, 21.617142857142856, 21.285, 21.034444444444443]

fig, ax = plt.subplots()
ax.plot(range(round(max(convergencia))), taxaMutacao[0], label = "Taxa de CrossOver = 0.3")
ax.plot(range(round(max(convergencia))), taxaMutacao[1], label = "Taxa de CrossOver = 0.6")
ax.plot(range(round(max(convergencia))), taxaMutacao[2], label = "Taxa de CrossOver = 0.9")
ax.set_xlabel("Convergência")  
ax.set_ylabel("Taxa de Mutação")
ax.legend()
matplotlib.pyplot.savefig("grafico")