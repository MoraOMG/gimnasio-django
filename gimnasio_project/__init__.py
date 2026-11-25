# PyMySQL se hace pasar por mysqlclient (evita compilar nada en Windows)
import pymysql

pymysql.install_as_MySQLdb()
