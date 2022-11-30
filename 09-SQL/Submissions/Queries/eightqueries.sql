--Queries
--1 List the following for each employee: emp_num, last_name, first_name, emp_sex, salary
SELECT
	e.emp_no as employee_num,
	e.last_name,
	e.first_name,
	e.gender,
	s.salary
FROM
	employees e
	join salaries s on e.emp_no = s.emp_no
ORDER BY
	e.last_name asc
;
--Code ran correctly



--2 List the first, last names and hire dates of employees hires in 1986
SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31';
--Code ran correctly



--3 Manager for each dept with the following: dept_num, dept_name, managers emp_num, last_name, first_name
SELECT d.dept_no, d.dept_name, e.last_name, e.first_name
FROM departments d
JOIN dept_manager dm ON (d.dept_no = dm.dept_no)
JOIN employees e ON (dm.emp_no = e.emp_no);

--CODE DID NOT RUN CORRECTLY using profs format, ran correctly this way


--4 dept of each emp with the following: emp_num, last_name, first_name and dept_name.
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e
JOIN dept_emp de ON (e.emp_no = de.emp_no)
JOIN departments d ON (de.dept_no = d.dept_no);
--Code ran correctly

--5 first_name, last_name, sex for employees with first name "hercules" and last name beginning with "B"
SELECT first_name, last_name, gender
FROM employees
WHERE first_name = 'Hercules'
AND last_name LIKE 'B%';
--Code ran correctly


--6 All employees in the Sales department include emp_num, last_name, first_name and dept_name
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e
JOIN dept_emp de ON (e.emp_no = de.emp_no)
JOIN departments d ON (de.dept_no = d.dept_no)
WHERE d.dept_name = 'Sales';

--7 All employess in Sales and Development departments include emp_num, last_name, first_name and dept_name
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e
JOIN dept_emp de ON (e.emp_no = de.emp_no)
JOIN departments d ON (de.dept_no = d.dept_no)
WHERE d.dept_name = 'Sales'
OR d.dept_name = 'Development';
--Code ran correctly

--8 List the frequency count of employee last_name (how many share each last_name) in descending order.
SELECT count(last_name) as frequency, last_name
FROM employees
GROUP BY last_name
ORDER BY count(last_name) DESC;
--Code ran correctly






