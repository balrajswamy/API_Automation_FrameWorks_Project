#it contains all end points and urls

class APIConstants():

    def base_url(self):

        return "https://restful-booker.herokuapp.com"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    def url_patch_put_delete(self, bookingid):
        return "https://restful-booker.herokuapp.com/booking/"+str(bookingid)