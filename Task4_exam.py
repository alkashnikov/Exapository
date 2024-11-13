{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "baecfa37-fb5c-4863-8b90-2ad263542bb0",
   "metadata": {},
   "outputs": [],
   "source": [
    "%%sql\n",
    "SELECT \n",
    "    d.DEPARTMENT_NAME AS \"Department Name\",\n",
    "    m.FIRST_NAME  ' '  m.LAST_NAME AS \"Manager Name\",\n",
    "    COUNT(e.EMPLOYEE_ID) AS \"Employee Count\"\n",
    "FROM \n",
    "    Departments d\n",
    "LEFT JOIN \n",
    "    Employees m ON d.MANAGER_ID = m.EMPLOYEE_ID\n",
    "LEFT JOIN \n",
    "    Employees e ON d.DEPARTMENT_ID = e.DEPARTMENT_ID\n",
    "GROUP BY \n",
    "    d.DEPARTMENT_NAME, m.FIRST_NAME, m.LAST_NAME\n",
    "ORDER BY \n",
    "    d.DEPARTMENT_NAME;"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
