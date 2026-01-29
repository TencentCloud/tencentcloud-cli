**Example 1: 创建数据表**



Input: 

```
tccli tcb RunSql --cli-unfold-argument  \
    --EnvId lowcode-2gqvfid5936609f4 \
    --Sql 
    CREATE TABLE `demo_users` (
        `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
        `username` VARCHAR(64) NOT NULL COMMENT '用户名',
        `email` VARCHAR(128) NULL COMMENT '邮箱',
        `status` TINYINT NOT NULL DEFAULT 1 COMMENT '状态：1-正常，0-禁用',
        `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
        `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
        PRIMARY KEY (`id`),
        UNIQUE KEY `uk_username` (`username`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表'
     \
    --DbInstance.EnvId lowcode-2gqvfid5936609f4 \
    --DbInstance.InstanceId  \
    --DbInstance.Schema lowcode-2gqvfid5936609f4
```

Output: 
```
{
    "Response": {
        "RequestId": "71aab888-21a1-4871-99d7-de6d418b4558",
        "Infos": [],
        "Items": [],
        "RowsAffected": 0
    }
}
```

**Example 2:  添加索引**



Input: 

```
tccli tcb RunSql --cli-unfold-argument  \
    --EnvId lowcode-2gqvfid5936609f4 \
    --Sql ALTER TABLE `demo_users` ADD INDEX `idx_email` (`email`) \
    --DbInstance.EnvId lowcode-2gqvfid5936609f4 \
    --DbInstance.InstanceId  \
    --DbInstance.Schema lowcode-2gqvfid5936609f4
```

Output: 
```
{
    "Response": {
        "RequestId": "aacad0bc-4107-4ddf-bd08-b401a925bb78",
        "RowsAffected": 0,
        "Infos": [],
        "Items": []
    }
}
```

**Example 3:  查询表结构**



Input: 

```
tccli tcb RunSql --cli-unfold-argument  \
    --EnvId lowcode-2gqvfid5936609f4 \
    --Sql SHOW FULL COLUMNS FROM `lowcode-2gqvfid5936609f4`.`demo_users` \
    --DbInstance.EnvId lowcode-2gqvfid5936609f4 \
    --DbInstance.InstanceId  \
    --DbInstance.Schema lowcode-2gqvfid5936609f4
```

Output: 
```
{
    "Response": {
        "RequestId": "b84801f8-439d-4fa6-885c-3011ab9cc3a0",
        "Infos": [
            "{\"databaseType\":\"VARCHAR\",\"length\":0,\"name\":\"Field\",\"nullable\":false,\"precision\":0,\"scale\":0}",
            "{\"databaseType\":\"TEXT\",\"length\":0,\"name\":\"Type\",\"nullable\":false,\"precision\":0,\"scale\":0}",
            "{\"databaseType\":\"VARCHAR\",\"length\":0,\"name\":\"Collation\",\"nullable\":true,\"precision\":0,\"scale\":0}",
            "{\"databaseType\":\"VARCHAR\",\"length\":0,\"name\":\"Null\",\"nullable\":false,\"precision\":0,\"scale\":0}",
            "{\"databaseType\":\"VARCHAR\",\"length\":0,\"name\":\"Key\",\"nullable\":false,\"precision\":0,\"scale\":0}",
            "{\"databaseType\":\"TEXT\",\"length\":0,\"name\":\"Default\",\"nullable\":true,\"precision\":0,\"scale\":0}",
            "{\"databaseType\":\"VARCHAR\",\"length\":0,\"name\":\"Extra\",\"nullable\":false,\"precision\":0,\"scale\":0}",
            "{\"databaseType\":\"VARCHAR\",\"length\":0,\"name\":\"Privileges\",\"nullable\":false,\"precision\":0,\"scale\":0}",
            "{\"databaseType\":\"VARCHAR\",\"length\":0,\"name\":\"Comment\",\"nullable\":false,\"precision\":0,\"scale\":0}"
        ],
        "Items": [
            "{\"Collation\":null,\"Comment\":\"主键ID\",\"Default\":null,\"Extra\":\"auto_increment\",\"Field\":\"id\",\"Key\":\"PRI\",\"Null\":\"NO\",\"Privileges\":\"select,insert,update,references\",\"Type\":\"bigint(20)\"}",
            "{\"Collation\":\"utf8mb4_general_ci\",\"Comment\":\"用户名\",\"Default\":null,\"Extra\":\"\",\"Field\":\"username\",\"Key\":\"UNI\",\"Null\":\"NO\",\"Privileges\":\"select,insert,update,references\",\"Type\":\"varchar(64)\"}",
            "{\"Collation\":\"utf8mb4_general_ci\",\"Comment\":\"邮箱\",\"Default\":null,\"Extra\":\"\",\"Field\":\"email\",\"Key\":\"\",\"Null\":\"YES\",\"Privileges\":\"select,insert,update,references\",\"Type\":\"varchar(128)\"}",
            "{\"Collation\":null,\"Comment\":\"状态：1-正常，0-禁用\",\"Default\":\"1\",\"Extra\":\"\",\"Field\":\"status\",\"Key\":\"\",\"Null\":\"NO\",\"Privileges\":\"select,insert,update,references\",\"Type\":\"tinyint(4)\"}",
            "{\"Collation\":null,\"Comment\":\"创建时间\",\"Default\":\"CURRENT_TIMESTAMP\",\"Extra\":\"\",\"Field\":\"created_at\",\"Key\":\"\",\"Null\":\"NO\",\"Privileges\":\"select,insert,update,references\",\"Type\":\"timestamp\"}",
            "{\"Collation\":null,\"Comment\":\"更新时间\",\"Default\":\"CURRENT_TIMESTAMP\",\"Extra\":\"on update CURRENT_TIMESTAMP\",\"Field\":\"updated_at\",\"Key\":\"\",\"Null\":\"NO\",\"Privileges\":\"select,insert,update,references\",\"Type\":\"timestamp\"}"
        ],
        "RowsAffected": 0
    }
}
```

**Example 4: 查询所有数据表名**



Input: 

```
tccli tcb RunSql --cli-unfold-argument  \
    --EnvId lowcode-2gqvfid5936609f4 \
    --Sql 
    SELECT TABLE_NAME, TABLE_COMMENT
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'demo_schema' AND TABLE_TYPE = 'BASE TABLE'
     \
    --DbInstance.EnvId lowcode-2gqvfid5936609f4 \
    --DbInstance.InstanceId demo_conn \
    --DbInstance.Schema demo_schema
```

Output: 
```
{
    "Response": {
        "RequestId": "d2f65ab5-90b8-4302-94f7-fed040f11a61",
        "Infos": [
            "{\"databaseType\":\"VARCHAR\",\"length\":0,\"name\":\"TABLE_NAME\",\"nullable\":true,\"precision\":0,\"scale\":0}",
            "{\"databaseType\":\"VARCHAR\",\"length\":0,\"name\":\"TABLE_COMMENT\",\"nullable\":true,\"precision\":0,\"scale\":0}"
        ],
        "Items": [
            "{\"TABLE_COMMENT\":\"用户表\",\"TABLE_NAME\":\"demo_users\"}"
        ],
        "RowsAffected": 0
    }
}
```

**Example 5: 删除数据表**



Input: 

```
tccli tcb RunSql --cli-unfold-argument  \
    --EnvId lowcode-2gqvfid5936609f4 \
    --Sql DROP TABLE IF EXISTS `demo_users` \
    --DbInstance.EnvId lowcode-2gqvfid5936609f4 \
    --DbInstance.InstanceId  \
    --DbInstance.Schema lowcode-2gqvfid5936609f4
```

Output: 
```
{
    "Response": {
        "RequestId": "51272b35-b345-4164-b7ed-13c2d0e203c6",
        "Infos": [],
        "Items": [],
        "RowsAffected": 0
    }
}
```

