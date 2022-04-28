class Ordering:
    def __init__(self , obj , paginator=False):
        self.objects = obj 
        self.paginition = paginator

    def order_obj(self , order , type):
        if order != None and type != None:
            if type == 'asc':
                new_order = f'-{order}'
            elif type == 'desc':
                new_order = f'{order}'
            else:
                # self.filter_obj(order,type)
                print(getattr(order))
            return self.objects.order_by(new_order)
        else: 
            return self.objects

    # def filter_obj(self , order , type):
    #     if order == 
    #     return self.objects.filter(new_order=new_type)

    def paginator_obj(self):
        pass
