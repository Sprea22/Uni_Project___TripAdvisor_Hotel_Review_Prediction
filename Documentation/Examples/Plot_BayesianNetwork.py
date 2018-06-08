from matplotlib import rc
rc("font", family="serif", size=12)
rc("text", usetex=True)

import daft

pgm = daft.PGM([3.6, 2.7], origin=[1.15, 0.65])
pgm.add_node(daft.Node("Lil Pump", r"Lil Pump", 3, 3, aspect=2.4))
pgm.add_node(daft.Node("Money", r"Money", 2, 2, aspect=2.1))
pgm.add_node(daft.Node("Drugs", r"Drugs", 4, 2, aspect=2.1))
pgm.add_node(daft.Node("Esghere", r"Esghere", 3, 1, aspect=2.4, observed=True))
pgm.add_edge("Lil Pump", "Money")
pgm.add_edge("Lil Pump", "Drugs")
pgm.add_edge("Money", "Esghere")
pgm.add_edge("Drugs", "Esghere")
pgm.render()
pgm.figure.savefig("ImageBayesianNet.pdf")
pgm.figure.savefig("ImageBayesianNet.png", dpi=150)
