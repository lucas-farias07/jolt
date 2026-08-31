from datetime import date


class Task:
    def __init__(self, description: str, done: bool, deadline: date = date.min):
        self.__desc = description
        self.__is_done = done
        self.__deadline = deadline

    @property
    def description(self) -> str:
        return self.__desc

    @property
    def is_done(self) -> bool:
        return self.__is_done

    def change_status(self) -> bool:
        """ Changes the task's status (done to undone, undone to done)
            Returns: <bool> (The present status)
        """
        self.__is_done = not self.__is_done

        return self.__is_done
