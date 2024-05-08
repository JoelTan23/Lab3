import employee_info as employee_info

def test_employee_by_age_range():
    result = employee_info.get_employees_by_age_range(24,26)
	
    assert (result ==[{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}])
	
def test_calculate_average_salary():
	result = round(employee_info.calculate_average_salary(),2)
	
	assert (result == round(60166.66666666666,2) )
	
def test_get_employees_by_dept():
	result = employee_info.get_employees_by_dept("Engineering")
	
	assert (result==[{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}])