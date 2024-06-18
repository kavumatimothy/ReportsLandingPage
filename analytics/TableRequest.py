from .DBservice import DbService


class TableRequest:
    def __init__(self, config):
        self.__status_code = 0
        self.__config = config
        self.__reports = []

    def get_table(self):
        try:
            for each_endpoint in self.__config["endpoints"]:
                table_name = each_endpoint["report_name"]
                database = each_endpoint["db_name"]
                user = each_endpoint["db_user"]
                password = each_endpoint["db_password"]
                host = each_endpoint["db_host"]
                port = each_endpoint["db_port"]

                db_service = DbService(database, user, password, host, port)
                table_df = db_service.get_from_db(table_name)
                return table_df
        except Exception as e:
            print("error", e)


