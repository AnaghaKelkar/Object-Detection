# Object Detection using Haar Classifier

Haar classifier is a machine learning based approach , an algorithm created by Paul Viola and Michael Jones.
Trained from many positive images (with faces) and negative images (without faces).

It starts by extracting Haar features from each image by above windows. Each window is placed on the picture to calculate a single feature. This feature is single value obtained by subtracting sum of pixels under white part of the window from the sum of pixels under the black part of the window.
Now, all possible sizes of each window are placed on all possible locations of each image to calculate plenty of features.

OpenCV:
-------

OpenCV is the most popular library for computer vision.
OpenCV uses machine learning algorithms to search for faces within a picture. Because faces are so complicated, there isn’t one simple test that will tell you if it found a face or not. Instead, there are thousands of small patterns and features that must be matched.

The algorithms break the task of identifying the face into thousands of smaller, bite-sized tasks, each of which is easy to solve. These tasks are also called Classifiers.

OpenCV uses cascades. What’s a cascade? The best answer can be found in the dictionary: “ a waterfall or series of waterfalls. “ Like a series of waterfalls, the OpenCV cascade breaks the problem of detecting faces into multiple stages. 

	- For each block, it does a very rough and quick test.
	
	- If that passes, it does a slightly more detailed test, and so on.

The algorithm may have 30 to 50 of these stages or cascades, and it will only detect a face if all stages pass.

The advantage is that the majority of the picture will return negative during the first few stages, which means the algorithm won’t waste time testing all 6000 features on it. 
