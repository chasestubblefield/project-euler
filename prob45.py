if __name__ == "__main__":
	limit = 100000
	triangles = [ n * (n+1) / 2 for n in range(1, limit+1) ]
	pentagons = [ n * (3*n - 1) / 2 for n in range(1, limit+1) ]
	hexagons = [ n * (2*n - 1) for n in range(1, limit+1) ]
	intersect = list(set(triangles) & set(pentagons) & set(hexagons))
	print intersect
