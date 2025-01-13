from database import create_con


class Task:
    def __init__(self, id, title, user_id, status=False):
        self.id = id
        self.title = title
        self.user_id = user_id
        self.status = status


class TaskRepo:
    __table_name = "task"

    def get(self, id: int):
        con = create_con()
        SQL = f"SELECT * FROM {self.__table_name} WHERE id = ?"
        query = con.execute(SQL, [id])
        data = query.fetchone()
        return Task(*data)

    def get_by_user_id(self, user_id):
        con = create_con()
        SQL = f"SELECT * FROM {self.__table_name} WHERE user_id = ?"
        query = con.execute(SQL, [user_id])
        data = query.fetchall()
        return [Task(*row) for row in data]

    def add_task(self, user_id: int, text: str):
        con = create_con()
        SQL = f"""
            INSERT INTO {self.__table_name}(title, user_id, status)
            VALUES (?, ?, ?)
        """
        con.execute(
            SQL,
            [text, user_id, False],
        )
        con.commit()

    def update(self, updated_task: Task):
        con = create_con()
        SQL = f"""
            UPDATE {self.__table_name}
            SET title = ?,
                status = ?
            WHERE id = ?
        """
        con.execute(SQL, [
            updated_task.title, 
            updated_task.status, 
            updated_task.id
        ])
        con.commit()

    def delete(self, id):
        con = create_con()
        SQL = f"""
            DELETE FROM {self.__table_name}
            WHERE id = ?
        """
        con.execute(SQL, [id])
        con.commit()