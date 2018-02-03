blockSize = 11

#Binary threshold type
thresholdType = cv2.THRESH_BINARY

#Load an image
#cv2.IMREAD_COLOR = Default flag for imread. Loads color image.
#cv2.IMREAD_GRAYSCALE = Loads image as grayscale.
#cv2.IMREAD_UNCHANGED = Loads image which have alpha channels.
#cv2.IMREAD_ANYCOLOR = Loads image in any possible format
#cv2.IMREAD_ANYDEPTH = Loads image in 16-bit/32-bit otherwise converts it to 8-bit
input_img = cv2.imread(image_read_path,cv2.IMREAD_UNCHANGED)

#Check if image is loaded 
if input_img is not None:
	#Create a Window
	#cv2.WINDOW_NORMAL = Enables window to resize.
	#cv2.WINDOW_AUTOSIZE = Default flag. Auto resizes window size to fit an image.
	cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
	#Show image in window
	cv2.imshow(window_name,input_img)
	#Wait untill user enter any key
	cv2.waitKey(wait_time)
	#Destroy Window
	cv2.destroyWindow(window_name)
	
	print ("Hello, Welcome To Adaptive Threshold Operations")
	#Get the image dimesion in a tuple
	img_dimension= input_img.shape
	
	if img_dimension > 2:
		img_gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
	else:
		img_gray = input_img
	
	#Loop Forever
	while True:
		#Ask User to choose operation
		print ("Choose Your Operation:")
		print ("1. Adaptive Mean Thresholding")
		print ("2. Adaptive Gaussian Thresholding")
		print ("3. Exit")
		choice = None	
		#Loops untill user enters valid number
		while True:
			try:
				choice = int(input("Your Option: "))
				if  0 < choice < 4:
					break
				raise StandardError()	
			except:
				print("Please Enter Valid Number")		
		
		#Exit from the while loop
		if choice == 3:
			break
		
		#if user choose to get value
		elif choice == 1:
			adaptive_method = cv2.ADAPTIVE_THRESH_MEAN_C
		
		#if user choose to set value
		elif choice == 2:
			adaptive_method = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
		
		#cv2.adaptiveThreshold(src, maxValue, adaptive_method, thresholdType, blockSize, correction_constant)		
		#src: source input image
		#maxval: maximum value that image can have
		#adaptive_method: Adaptive Thresholding method
		#thresholdType: type of thresholding
		#blockSize: Size of pixels neighbourhoods used to calculate threshold
		#correction_constant: Constant subtacted from mean or weighted mean
		#dst: output image
		threshold_img = cv2.adaptiveThreshold(img_gray, maxval, adaptive_method, thresholdType , blockSize, correction_constant)
		#Create a Window
		cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
		#Show image in window
		cv2.imshow(window_name,img_gray)
		#Create a Window
		cv2.namedWindow(window_threshold_name,cv2.WINDOW_NORMAL)
		#Show image in window
		cv2.imshow(window_threshold_name,threshold_img)
		#Wait untill user enter any key
		cv2.waitKey(wait_time)  
		#Destroy All Window
		cv2.destroyAllWindows()
			
else:
	print ("Please Check The Path of Input File")