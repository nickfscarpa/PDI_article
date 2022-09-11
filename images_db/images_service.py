import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='teste'
)
cursor = connection.cursor()


def insertImage(filePath):
    with open(filePath, 'rb') as file:
        binaryData = file.read()
    insert_query = "INSERT INTO images (image) VALUES (%s)"
    cursor.execute(insert_query, (binaryData, ))
    connection.commit()


def retrieveImage(id):
    retrieve_query = "SELECT * FROM images WHERE id = '{0}'"
    cursor.execute(retrieve_query.format(str(id)))
    result = cursor.fetchone()[1]
    storeFilePath = "ImageOutputs/img{0}.jpg".format(str(id))
    print(result)
    with open(storeFilePath, "wb") as file:
        file.write(result)
        file.close()
