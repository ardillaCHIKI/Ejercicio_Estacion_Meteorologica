# class WeatherNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class StationNode:
#     def __init__(self, name):
#         self.name = name
#         self.sublist_head = None
#         self.next = None

#     def add_weather(self, data):
#         new_node = WeatherNode(data)
#         if not self.sublist_head:
#             self.sublist_head = new_node
#         else:
#             current = self.sublist_head
#             while current.next:
#                 current = current.next
#             current.next = new_node

# class StationList:
#     def __init__(self):
#         self.head = None

#     def add_station(self, name):
#         new_station = StationNode(name)
#         if not self.head:
#             self.head = new_station
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_station
#         return new_station