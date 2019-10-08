# Car Detection from satellite | Aerial image

<b>Dataset:</b> 
<ul>
	<li>Dataset was provided in EEUS2018 conference of Google Earth Engine.</li>
	<li>They have demonstrated how to export data from GEE as TFRecords.</li>
	<li>Developed a model to detect cars in 15cm aerial imagery.</li>
</ul>

<b>Model</b>
<ul>
	<li>
		First I tried with state of the art model VGG16 for classifying the image.
	</li>
	<li>
		VGG16 had a poor performance on the dataset. Maybe its because patch size of the images is relatively very small to be used with maxpool, which is used heavily in VGG16.
	</li>
	<li>
		Second Implementation gave very nice performance, in which I have ommited maxpool and applied batch normalization. 
		Train accuracy: 97%
		Test accuracy: 82%
	</li>
	<li>ResNet can be very good model, can be given a try as another variant.</li>
</ul>