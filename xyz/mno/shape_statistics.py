from xyz.mno.shape import Shape

class ShapeStatistics:

    # class function
    # Classname.functioncall()
    def getStats(shape):
        if isinstance(shape, Shape):
            area = shape.area()
            peri = shape.perimeter()

            return 'Area : {0}\nPerimeter: {1}'.format(area, peri)
        return -1
