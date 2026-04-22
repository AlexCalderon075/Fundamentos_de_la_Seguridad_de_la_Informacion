from PIL import Image
import numpy as np


imagen1 = np.asarray( Image.open('scrambled1.png') )
imagen2 = np.asarray( Image.open('scrambled2.png') )

print(imagen1)
print(imagen2)

data = imagen1.copy() + imagen2.copy()

nueva = Image.fromarray(data)
nueva.save("out.png", "PNG")

