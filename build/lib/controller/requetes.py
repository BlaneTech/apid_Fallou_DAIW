sql = {
    'user': "INSERT INTO USERS (userId,name,userName,userEmail,userPhone,userWebsite,addressId) VALUES (%s,%s,%s,%s,%s,%s,%s)",
    'address':"INSERT INTO ADDRESS (street, suite,city, zipcode,geo_lat,geo_lng) VALUES (%s,%s,%s,%s,%s,%s)",
    'company':"INSERT INTO COMPANY (companyName,companyCatchPhrase,companyBs,userId) VALUES (%s,%s,%s,%s)",
    'post':"INSERT INTO POSTS (postId,postTitle,postBody,userId) VALUES (%s,%s,%s,%s)",
    'comment':"INSERT INTO COMMENTS (commentId,commentName,commentEmail,commentBody,postId) VALUES (%s,%s,%s,%s,%s)",
    'album':"INSERT INTO ALBUMS (albumId,albumTitle,userId) VALUES (%s,%s,%s)",
    'photo': "INSERT INTO PHOTOS (photoId,photoTitle,photoUrl,photoThumbnailUrl,albumId) VALUES (%s,%s,%s,%s,%s)",
    'todo':"INSERT INTO TODOS (todoId,todoTitle,userId) VALUES (%s,%s,%s)",

    # 1:"SELECT * FROM USERS"
}

urlApi = {
    'user': "https://jsonplaceholder.typicode.com/users",
    'post':"https://jsonplaceholder.typicode.com/posts",
    'comment': "https://jsonplaceholder.typicode.com/comments",
    'album': "https://jsonplaceholder.typicode.com/albums",
    'photo':"https://jsonplaceholder.typicode.com/photos",
    'todo': "https://jsonplaceholder.typicode.com/todos"
}

