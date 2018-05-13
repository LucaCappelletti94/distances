from distances import euclidean, jensen_shannon, bhattacharyya, total_variation
from utils import create_cases

def test_symmetry():
    errors = []
    a,b = create_cases()
    for distance_name, distance in [("euclidean", euclidean), ("jensen_shannon", jensen_shannon), ("bhattacharyya", bhattacharyya), ("total_variation", total_variation)]:
       # replace assertions by conditions
        if distance(a,b) != distance(b,a):
            errors.append("Metric '%s' is not symmetric"%distance_name)

    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))