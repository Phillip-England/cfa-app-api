from models.HttpError import HttpError


def validate_number(self):
    try:
        int(self.number)
    except:
        raise HttpError(400, 'store number must be a number')
