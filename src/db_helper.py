import mysql.connector
# CREATE TABLE employee (
#                         emp_id INT NOT NULL,
#                         emp_name VARCHAR(100) NOT NULL,
#                         emp_salary INT NOT NULL,
#                         PRIMARY KEY (emp_id)
#                       );
class DbHelper:

    def __init__(self):
        user = ""
        password = ""
        try:
            self.conn = mysql.connector.connect(user=user, password=password,
                                          host='127.0.0.1',
                                          database='dg_mock_employees',
                                          use_pure=True)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        statement = "SELECT MAX(emp_salary) FROM employee"
        cursor = self.conn.cursor()
        cursor.execute(statement)
        r = cursor.fetchall()
        return int(r[0][0])

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        statement = "SELECT MIN(emp_salary) FROM employee"
        cursor = self.conn.cursor()
        cursor.execute(statement)
        r = cursor.fetchall()
        return int(r[0][0])


if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)