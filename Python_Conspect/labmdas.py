s = lambda a: a*a

print(s(4))

items_cost = [999, 888, 1100, 1200, 1300, 777]
gt_thousand = filter(lambda x : x > 1000, items_cost)
x = list(gt_thousand)
print("Eligible for discount: ", x)

without_gst_cost = [100, 200, 300, 400]
with_gst_cost = map(lambda x: x + 10, without_gst_cost)
x = list(with_gst_cost)
print("Without GST items costs: ", without_gst_cost)
print("With GST items costs: ", x)

from functools import reduce

each_items_costs = [111, 222, 333, 444]
total_cost = reduce(lambda x, y: x+y, each_items_costs)
print(total_cost)
