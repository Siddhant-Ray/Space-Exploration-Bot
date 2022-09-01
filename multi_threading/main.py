import kmeans,test,detect_bright_spots,read_sensor,feature_match,kmeans_test

from threading import Thread

t=Thread(target=detect_bright_spots.main('img1.jpg')).start()



t1=Thread(target=feature_match.main('two.jpg','mineral_ID.jpg','one.jpg')).start() 



t2=Thread(target=read_sensor.main('sampledata.csv')).start()
t2=Thread(target=kmeans_test.main()).start()

