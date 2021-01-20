create table if not exists `task`(
    `assginee` varchar(40) not null,
    `category` varchar(40) not null,
    `subject` varchar(1024) not null,
    `status` tinyint not null,
    `create_time` date,
    `end_time` date,
    primary key(``)
);

create table if not exists `category`(
    `title` varchar(32) not null,
    `sort`  int         not null,
    primary key(``)
);
