from colour_desc import colour_descriptors
import argparse
import glob
import cv2


from image_repository import settings


def create_database():
	database = 'image_features.csv'
	#init color desc
	cd = colour_descriptors((8, 12, 3))

	# open the output index file for writing
	output = open(database, "w")
	print(settings.MEDIA_ROOT + '/image_folder')
	# use glob to grab the image paths and loop over them
	for imagePath in glob.glob(settings.MEDIA_ROOT + '/image_folder/*'):
		# extract the image ID (i.e. the unique filename) from the image
		# path and load the image itself
		imageID = imagePath[imagePath.rfind("/") + 1:]
		print(imageID)
		image = cv2.imread(imagePath)

			# describe the image
		features = cd.describe(image)
		# write the features to file
		features = [str(f) for f in features]
		output.write("%s,%s\n" % (imageID, ",".join(features)))
	# close the index file
	output.close()

if __name__ == "__main__":
	print("running...")
	create_database()