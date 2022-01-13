import ee
#ee.Initialize()

# need to make sure all the other fires are not used to calculate the phenology offset
def addDate2Fire(feat):
    date = ee.Date(feat.get('fih_date1'))
    return feat.set('system:time_start', date)

# have to mask out other fires, then use reduce regions on the  b_difference
def add_union_props(feat):
    return feat.set('union', 1)

