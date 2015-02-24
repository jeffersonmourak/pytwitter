import pygame, sys
import pygame.camera
import time

def take_pic():
	diretorio = "/home/andrepsilva/"

	pygame.init()
	pygame.camera.init()
	cam = pygame.camera.Camera("/dev/video0", (640,480))

	cam.start()
	image = cam.get_image()
	cam.stop

	timestamp =time.strftime("%d-%m-%Y_%H-%M-%S", time.localtime())
	filename = "%s/%s.jpg" % (diretorio, timestamp)

	pygame.image.save(image, filename)
	print "Salvo"
