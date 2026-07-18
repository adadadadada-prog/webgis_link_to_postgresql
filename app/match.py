from app.s_line import store_line
from app.s_point import store_point
from app.s_polygon import store_polygon


def match_db(name,geodata):
    match name:
        case "Polygon":
            return store_polygon(geodata)
        case "Point":
            return store_point(geodata)
        case "LineString":
             return store_line(geodata)
