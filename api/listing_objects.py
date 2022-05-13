class Listing:
    def __init__(self,queryset):
        self.queryset = queryset
        

    def listing_obj(self, range):
        self.next_objects = int(range)
        self.previous_objects = self.next_objects - 10
        print(self.previous_objects , self.next_objects)
        return self.queryset[self.previous_objects:self.next_objects]
