

class Meme:

	def __init__(self, name, image, source, descr=None, tag=[], meme_type=None):
		self.name = name
		self.image = image
		self.source = source

		self.description = descr
		self.tag = tag
		self.meme_type = None

		self.date_created = ""
		self.date_origin = ""
		self.last_updated = ""

	def get_date_origin(self):
		# connect to database and get data
		return "today"