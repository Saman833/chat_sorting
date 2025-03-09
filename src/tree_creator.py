import json
def dfs(vertex, visited, v_neighbors , components, root):
    visited.add(vertex)
    components[root].append(vertex)
    for neighbor, weight in v_neighbors[vertex]:
        if neighbor not in visited:
            dfs(neighbor, visited, v_neighbors,root)
class Grap: 
    def __init__(self):
        pass 
        self.vertices=set()
        self.v_neighbors={}
        self.components={}
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.add(vertex)
            self.v_neighbors[vertex]=[]
    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.v_neighbors[vertex2].append((vertex1, weight))
    def find_components(self):
        visited=set()
        for vertex in self.vertices:
            if vertex not in visited:
                root=vertex
                self.components[vertex]=[]
                dfs(vertex, visited, self.v_neighbors, self.components, root)
def get_json_graph(file_path):
    try : 

        with open(file_path, 'r' , encoding="utf-8") as file:
            return  json.load(file)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
def create_graph(json_data:dict):
    graph=Grap()
    for message_id in json_data:
        graph.add_vertex(message_id)
    for message_id, message in json_data.items():
        if not message["replyTo"]==None:
            graph.add_edge(message_id, message["replyTo"])
    return graph
        
def main():
    file_path="messages_json_labeled.json"
    json_data= get_json_graph(file_path)
    graph=create_graph(json_data)
    graph.find_components()
    print(len(graph.components))
    
main()


