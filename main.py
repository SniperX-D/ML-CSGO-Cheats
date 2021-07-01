import argparse
import train
from detector import *
from screenshot import *

def main():

	parser = argparse.ArgumentParser(description='Running YOLOv4 netwrok against CSGO')

	parser.add_argument(

	'mode',
	default = 'Run_Cheats', 
	nargs='?',
	choices = ['Train','Run_Cheats'],
	help = 'run the cheats or train the netwrok',

	)

	parser.add_argument(

	'--dataset-path',
	default = './dataset/',
	help='path to your dataset'

	)

	parser.add_argument(

	'--yolo-cfg-file',
	default = './yolo-data/CSGO.cfg',
	help='yolo netwrok configuration file'

	)

	parser.add_argument(

	'--yolo-weights-file',
	default = './yolo-data/CSGO_best.weights',
	help = 'file that contains the trained weights for the yolo network'
	)

	parser.add_argument(

	'--yolo-data-file',
	default = './yolo-data/CSGO.data',
	help='yolo data file that contains number of classes, names file location, train path'

	)

	parser.add_argument(

	'--yolo-names-file',
	default = './yolo-data/CSGO.names',
	help='yolo object names list file'

	)

	args = parser.parse_args()

	if args.mode == 'Run_Cheats':
		s = screensoter("Counter-Strike: Global Offensive - OpenGL")  
		d = detector(args)
		while True:
		    open_cv_image = s.get_screenshot()
		    open_cv_image, detection_time = d.run(open_cv_image) # run detection!
		    fps = str(int(1/detection_time)) #calculate the time in seconds it took to detect this image
		    font = cv2.FONT_HERSHEY_SIMPLEX
		    cv2.putText(open_cv_image, "fps: %s"%fps, (7,40), font, 1, (100, 255, 0), 2, cv2.LINE_AA) #puts a FPS counter on the top
		    cv2.imshow('image',numpy.array(open_cv_image)) #show the image with detection boxes!
		    cv2.waitKey(1)    

	elif args.mode == 'Train':
		train.train(args)

if __name__ == '__main__':
	main()
