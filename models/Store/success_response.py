def success_response(self):
    return {
        "_id": self.id,
        'user': self.user,
        'name': self.name,
        'number': self.number
    }
