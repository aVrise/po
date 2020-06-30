import imageio
images = []
filenames = ['./0.png','./1.png','2.png','3.png','4.png','5.png']
for filename in filenames:
    images.append(imageio.imread(filename))
# imageio.help(gif)
imageio.mimsave('movie.gif', images, duration = 0.1)