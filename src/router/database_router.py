class DatabaseRouter:

    MYSQL_TABLES = [

        "employees",

        "departments",

        "customers",

        "orders",

        "order_items",

        "products"

    ]

    MONGO_COLLECTIONS = [

        "employees",

        "customers",

        "orders",

        "products"

    ]

    @staticmethod
    def detect(question: str):

        question = question.lower()

        # Explicit Mongo

        if "mongodb" in question:

            return "MongoDB"

        # Explicit SQL

        if "mysql" in question:

            return "MySQL"

        # Collections / Tables

        for name in DatabaseRouter.MONGO_COLLECTIONS:

            if name in question:

                # if both databases contain same name,
                # keep MySQL as default

                return "MySQL"

        return "MySQL"