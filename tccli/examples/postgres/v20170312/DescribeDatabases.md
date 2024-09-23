**Example 1: 获取实例所有数据库**

不做筛选，全量拉取实例的数据库列表。

Input: 

```
tccli postgres DescribeDatabases --cli-unfold-argument  \
    --DBInstanceId postgres-hf8jo5pr
```

Output: 
```
{
    "Response": {
        "Items": [
            "postgres",
            "postgres_bak_1715086333",
            "postgres_bak_1715140150",
            "rds",
            "postgres_bak_1715152994"
        ],
        "Databases": [
            {
                "DatabaseName": "postgres",
                "DatabaseOwner": "postgres",
                "Encoding": "UTF8",
                "Collate": "C",
                "Ctype": "C",
                "AllowConn": true,
                "ConnLimit": -1,
                "Privileges": "=Tc/postgres,postgres=CTc/postgres,pg_tencentdb_superuser=C/postgres"
            },
            {
                "DatabaseName": "postgres_bak_1715086333",
                "DatabaseOwner": "postgres",
                "Encoding": "UTF8",
                "Collate": "C",
                "Ctype": "C",
                "AllowConn": true,
                "ConnLimit": -1,
                "Privileges": ""
            },
            {
                "DatabaseName": "postgres_bak_1715140150",
                "DatabaseOwner": "postgres",
                "Encoding": "UTF8",
                "Collate": "C",
                "Ctype": "C",
                "AllowConn": true,
                "ConnLimit": -1,
                "Privileges": ""
            },
            {
                "DatabaseName": "rds",
                "DatabaseOwner": "postgres",
                "Encoding": "UTF8",
                "Collate": "C",
                "Ctype": "C",
                "AllowConn": true,
                "ConnLimit": -1,
                "Privileges": ""
            },
            {
                "DatabaseName": "postgres_bak_1715152994",
                "DatabaseOwner": "postgres",
                "Encoding": "UTF8",
                "Collate": "C",
                "Ctype": "C",
                "AllowConn": true,
                "ConnLimit": -1,
                "Privileges": ""
            }
        ],
        "RequestId": "4045d7a9-5330-4c2c-b968-475570200a97",
        "TotalCount": 5
    }
}
```

**Example 2: 获取实例部分数据库**

使用筛选条件，返回部分数据库列表。

Input: 

```
tccli postgres DescribeDatabases --cli-unfold-argument  \
    --DBInstanceId postgres-hf8jo5pr \
    --Filters.0.Name database-name \
    --Filters.0.Values postgres \
    --Offset 1 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "Items": [
            "postgres_bak_1715086333",
            "postgres_bak_1715140150"
        ],
        "Databases": [
            {
                "DatabaseName": "postgres_bak_1715086333",
                "DatabaseOwner": "postgres",
                "Encoding": "UTF8",
                "Collate": "C",
                "Ctype": "C",
                "AllowConn": true,
                "ConnLimit": -1,
                "Privileges": ""
            },
            {
                "DatabaseName": "postgres_bak_1715140150",
                "DatabaseOwner": "postgres",
                "Encoding": "UTF8",
                "Collate": "C",
                "Ctype": "C",
                "AllowConn": true,
                "ConnLimit": -1,
                "Privileges": ""
            }
        ],
        "RequestId": "25cc2555-14a2-454f-af08-6bd691315335",
        "TotalCount": 5
    }
}
```

