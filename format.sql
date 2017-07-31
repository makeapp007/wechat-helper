CREATE TABLE TB_TICKETINFO(
   tid INT PRIMARY KEY     NOT NULL,
   tname           TEXT    NOT NULL,
   temail        CHAR(50),
   tcell        INT NOT NULL,
   tstatus    INT NOT NULL,
   wechatID   CHAR(50)
);
