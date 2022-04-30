class Ordering:
    def __init__(self , request , queryset=None):
        self.request = request
        self.objects = queryset 
        self.order = self.request.get("order") 
        self.type = self.request.get("order_type") 
        self.base = self.request.get("base") 

    def order_obj(self):
        if self.order != None and self.type != None:
            if self.base == 'ascending':
                new_order = f'-{self.type}'
            elif self.base == 'descending':
                new_order = f'{self.type}'
            return self.objects.order_by(new_order)
        else: 
            return self.objects
