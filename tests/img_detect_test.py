import pycda

from pycda import CDA, load_image

cda = CDA()
image = load_image('images/holdout_tile.pgm')
prediction = cda.get_prediction(image, verbose=True)
# print(prediction)
# prediction.show()
prediction.set_scale(7.5)
prediction.show()
detections = cda.predict(image, verbose=True)
print(detections.head(10))
prediction.show_detection()

from pycda.error_stats import ErrorAnalyzer
from pycda.sample_data import get_sample_csv

prediction.known_craters = get_sample_csv()
an = ErrorAnalyzer()
an.analyze(prediction)
an.show()
an.plot_densities()
