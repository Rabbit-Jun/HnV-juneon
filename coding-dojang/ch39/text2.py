class TimeIterator:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
        
    
    def __getitem__(self,index):
        if self.start+index <self.stop:
            start=self.start
            start +=index
            h=start//60**2
            m=start//60
            s=start%60

            if m >59:
                remain=m//60
                m-=remain*60
                h +=remain
            
            if h > 23:
                remain=h//24
                h -=remain*24
            
            
            
            return '%02d:%02d:%02d'%(h,m,s) 
         
        else:
            raise IndexError






start,stop,index = map(int, input().split())

 
for i in TimeIterator(start, stop):
    print(i)
 
print('\n', TimeIterator(start, stop)[index], sep='')