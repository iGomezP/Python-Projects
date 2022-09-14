from __future__ import print_function
from database.db import get_connection
from .entities.Movie import Movie


class MovieModel():

    # Para que se llame sin la necesidad de instanciar la clase MovieModel
    @classmethod
    def get_movies(self):
        try:
            connection = get_connection()
            movies = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, title, duration, released FROM movie ORDER BY title ASC")
                resultSet = cursor.fetchall()

                # Se recorre cada resultado como se asigna al array vacío movies
                for row in resultSet:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movies.append(movie.to_JSON())
            # Se cierra la conexión a la BD
            connection.close()
            # Devuelve la lista
            return movies
        except Exception as ex:
            raise Exception(ex)

    # Para que se llame sin la necesidad de instanciar la clase MovieModel
    @classmethod
    def get_movie(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, title, duration, released FROM movie WHERE id = %s", (id,))
                row = cursor.fetchone()

                movie = None
                if row != None:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movie = movie.to_JSON()

            # Se cierra la conexión a la BD
            connection.close()
            # Devuelve la lista
            return movie
        except Exception as ex:
            raise Exception(ex)

    # Para que se llame sin la necesidad de instanciar la clase MovieModel
    @classmethod
    def add_movie(self, movie):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO movie (id, title, duration, released) 
                               VALUES (%s, %s, %s, %s)""", (movie.id, movie.title, movie.duration, movie.released))

                affected_rows = cursor.rowcount
                # Confirmar cambios en la BD
                connection.commit()

            # Se cierra la conexión a la BD
            connection.close()
            # Devuelve la lista
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    # Para que se llame sin la necesidad de instanciar la clase MovieModel
    @classmethod
    def delete_movie(self, movie):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM movie WHERE id = %s", (movie,))

                # Recibe 1 como file afectada
                affected_rows = cursor.rowcount
                # Confirmar cambios en la BD
                connection.commit()

            # Se cierra la conexión a la BD
            connection.close()
            # Devuelve la lista
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    # Para que se llame sin la necesidad de instanciar la clase MovieModel
    @classmethod
    def update_movie(self, movie):
        try:
            connection = get_connection()
            print(movie.id)

            with connection.cursor() as cursor:
                cursor.execute("UPDATE movie SET title = %s, duration = %s, released = %s WHERE id = %s ", (
                    movie.title, movie.duration, movie.released, movie.id))

                affected_rows = cursor.rowcount
                # Confirmar cambios en la BD
                connection.commit()

            # Se cierra la conexión a la BD
            connection.close()
            # Devuelve la lista
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
