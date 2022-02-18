# Solution approach to a simple investments allocation problem solved
# with a LP model and Google OR-tools, including a sensitivity analysis
# Dimitris Rizopoulos, 2022

from ortools.linear_solver import pywraplp


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['constraint_coeffs'] = [
        [1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0.25, 0.25, -1],
        [-0.6, 0.4, 0, 0, 0],
    ]
    data['bounds'] = [142600.0, 60300.0, 82300.0, 0.0, 0.0]
    data['obj_coeffs'] = [0.025, 0.065, 0.072, 0.074, 0.037]
    data['num_vars'] = 5
    data['num_constraints'] = 5
    return data


def main():
    data = create_data_model()
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # declaration of decision variables
    infinity = solver.infinity()
    X = {}
    for j in range(data['num_vars']):
        X[j] = solver.NumVar(0, infinity, 'X[%i]' % j)
    print('Number of variables =', solver.NumVariables())

    # declaration of problem constraints
    constraint_list = []
    for i in range(data['num_constraints']):
        constraint = solver.RowConstraint(0, data['bounds'][i], '')
        for j in range(data['num_vars']):
            constraint.SetCoefficient(X[j], data['constraint_coeffs'][i][j])
        constraint_list.append(constraint)
    print('Number of constraints =', solver.NumConstraints())

    # Setting the objective function
    objective = solver.Objective()
    for j in range(data['num_vars']):
        objective.SetCoefficient(X[j], data['obj_coeffs'][j])
    objective.SetMaximization()

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print()
        print("Optimal solution calcualted:")
        print('Objective value =', solver.Objective().Value())
        for j in range(data['num_vars']):
            print(X[j].name(), ' = ', X[j].solution_value())
        print()
        print('Problem solved in %f milliseconds' % solver.wall_time())
        print('Problem solved in %d iterations' % solver.iterations())
        print()
        print("Reduced costs for decision varibles:")
        for index in X:
            variable = X[index]
            print(('%s: reduced cost = %f' % (variable.name(), variable.reduced_cost())))
        print()
        print("Shadow prices and activity for each constraint:")
        activities = solver.ComputeConstraintActivities() # get some of LHS of constraint
        for i, constraint in enumerate(constraint_list):
            print(('constraint %d: dual value = %f, activity = %f' %
              (i, constraint.dual_value(), activities[constraint.index()])))
    else:
        print('The problem does not have an optimal solution.')


if __name__ == '__main__':
    main()
 