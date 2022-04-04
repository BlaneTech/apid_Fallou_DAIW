DROP DATABASE IF EXISTS JSONPlaceholder;
CREATE DATABASE JSONPlaceholder;
USE JSONPlaceholder;

DROP Table IF EXISTS USERS;
CREATE Table USERS(
    userId INT,
    name VARCHAR(255),
    userName VARCHAR(255),
    userEmail VARCHAR(255),
    userPhone VARCHAR(255),
    userWebsite  VARCHAR(255),
    addressId INT,
    PRIMARY KEY(userId)
);
DROP Table IF EXISTS COMPANY;
CREATE Table COMPANY(
    companyId INT AUTO_INCREMENT,
    companyName VARCHAR(255),
    companyCatchPhrase VARCHAR(255),
    companyBs VARCHAR(255),
    userId INT,
    PRIMARY KEY(companyId)
);

DROP Table IF EXISTS ADDRESS;
CREATE Table ADDRESS(
    addressId INT AUTO_INCREMENT,
    street VARCHAR(255),
    suite VARCHAR(255),
    city VARCHAR(255),
    zipcode VARCHAR(255),
    geo_lat VARCHAR(255),
    geo_lng VARCHAR(255),
    PRIMARY KEY(addressId)
);

DROP Table IF EXISTS POSTS;
CREATE Table POSTS(
    postId INT ,
    postTitle VARCHAR(255),
    postBody TEXT,
    userId INT,
    PRIMARY KEY(postId)
);

DROP Table IF EXISTS COMMENTS;
CREATE Table COMMENTS(
    commentId INT ,
    commentName VARCHAR(255),
    commentEmail VARCHAR(255),
    commentBody TEXT,
    postId INT,
    PRIMARY KEY(commentId)
);

DROP Table IF EXISTS ALBUMS;
CREATE Table ALBUMS(
    albumId INT,
    albumTitle VARCHAR(255),
    userId INT,
    PRIMARY KEY(albumId)
) ;

DROP Table IF EXISTS PHOTOS;
CREATE Table PHOTOS(
    photoId INT,
    photoTitle VARCHAR(255),
    photoUrl VARCHAR(255),
    photoThumbnailUrl VARCHAR(255),
    albumId INT,
    PRIMARY KEY(photoId)
);

DROP Table IF EXISTS TODOS;
CREATE Table TODOS(
    todoId INT,
    todoTitle VARCHAR(255),
    userId INT,
    PRIMARY KEY(todoId)
);

ALTER Table USERS ADD CONSTRAINT FK_address FOREIGN KEY (addressId) REFERENCES ADDRESS(addressId);
ALTER Table COMPANY ADD CONSTRAINT FK_company FOREIGN KEY (userId) REFERENCES USERS(userId);
ALTER Table POSTS ADD CONSTRAINT FK_post FOREIGN KEY (userId) REFERENCES USERS(userId);
ALTER Table COMMENTS ADD CONSTRAINT FK_comment FOREIGN KEY(postId) REFERENCES POSTS(postId);
ALTER Table ALBUMS ADD CONSTRAINT FK_album FOREIGN KEY (userId) REFERENCES USERS(userId);
ALTER Table PHOTOS ADD CONSTRAINT FK_photo FOREIGN KEY (albumId) REFERENCES ALBUMS(albumId);
ALTER Table TODOS ADD CONSTRAINT FK_todos FOREIGN KEY (userId) REFERENCES USERS(userId);


