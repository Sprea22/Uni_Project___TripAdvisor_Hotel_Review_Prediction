from matplotlib import rc
import daft
from PIL import Image, ImageOps, ImageDraw

rc("font", family="serif", size=5)
rc("text", usetex=True)

pgm = daft.PGM([8, 2.5], origin=[0.8, 0.65])
pgm.add_node(daft.Node("Overall", "Overall", 4.8, 2.5, aspect=1))

term = ["Term1","...","TermN","Value","Rooms","Location","Clean.","Check in","Service","B.service"] #termini e metadati da inserire

i = 0
x = 1.2
while i < len(term):
  #print term[i]
  pgm.add_node(daft.Node(term[i], term[i], x, 1.5, aspect=1))
  pgm.add_edge("Overall", term[i])
  x = x + 0.8
  i = i + 1

pgm.render()
pgm.figure.savefig("ImageBayesianNet.pdf")
pgm.figure.savefig("ImageBayesianNet.png", dpi=200) #dpi ZOOM image (dimensione)
