def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	if len(a) == len(b):
		return [x + y for x, y in zip(a, b)]
	return -1