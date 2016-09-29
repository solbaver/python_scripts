from sets import Set

filename = 'mesh_50'

#creating a set of connected vertices
def get_indexes_of_vertexes():
	obj_file = open(filename+'.obj', 'r')
	index_array = Set([])
	for line in obj_file:
		if line[0] == 'f':
			#checking which vertices in the polygon
			face = map(int,line[1:].split())
			for vertex_index in face:
				index_array.add(vertex_index) 
	obj_file.close()
	return index_array 

#copying to memory array of all vertex
def create_array_of_vertexes(index_array):
	vertexes = []
	obj_file = open(filename+'.obj', 'r')
	#variables for number of one vertex before and afther deleting
	old_i = 1
	new_i = 1
	for line in obj_file:
		if line[0] == 'v':
			coords = map(float,line[1:].split())
			#if this vertex is connected to any face
			if old_i in index_array:
				element = (old_i, new_i, coords)
				new_i = new_i + 1
				vertexes.append(element)
			else:
				element = (old_i, 'delete', coords)
				vertexes.append(element)
			old_i = old_i + 1
	obj_file.close()
	return vertexes


#copying to memory array of all faces and changing vertices numbers from old to new
def faces_redefenition(verts_array):
	faces = []
	i = 1
	obj_file = open(filename+'.obj', 'r')
	for line in obj_file:
		if line[0] == 'f':	
			old_verts = map(int,line[1:].split())
			new_verts = []
			for vertex in old_verts:
				array_element = verts_array[vertex-1]
				new_verts.append(array_element[1])
			element = (i, new_verts)
			faces.append(element)
			i = i + 1
	obj_file.close()
	return faces

#writing data to new .obj file
def write_to_new_obj(verts_array, faces_array):
	i = 1
	new_obj_file = open(filename+'_new'+'.obj', 'w')
	for vert in verts_array:
		if vert[1] != 'delete':
			new_obj_file.write('v ' + str((vert[2])[0]) + ' ' + str((vert[2])[1]) + ' ' + str((vert[2])[2]) + ' ' + '\n')			
	for face in faces_array:
		#checing number of vertex in face - 3 or 4
		if len(face[1]) == 3:
			new_obj_file.write('f ' + str((face[1])[0]) + ' ' + str((face[1])[1]) + ' ' + str((face[1])[2]) + ' ' + '\n')
		if len(face[1]) == 4:
			new_obj_file.write('f ' + str((face[1])[0]) + ' ' + str((face[1])[1]) + ' ' + str((face[1])[2]) + ' ' + str((face[1])[4]) + ' '  + '\n')
	new_obj_file.close()
		
index_array = get_indexes_of_vertexes()		
verts_array = create_array_of_vertexes(index_array)
faces_array = faces_redefenition(verts_array)
write_to_new_obj(verts_array, faces_array)
