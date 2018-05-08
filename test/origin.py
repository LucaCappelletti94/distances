from distances import euclidean
from .test_utils import test_cases

def test_origin():
    errors = []
    a = test_case()
    for distance_name, distance in [("euclidean", euclidean)]:
       # replace assertions by conditions
        if distance(a,a) != 0:
            errors.append("Metric '%s' is not null on same point"%distance_name)

    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))