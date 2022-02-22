**Example 1: 查询指定实例的表结构**



Input: 

```
tccli mariadb DescribeDatabaseTable --cli-unfold-argument  \
    --InstanceId tdsql-e9tklsgz \
    --DbName test \
    --Table region
```

Output: 
```
{
    "Response": {
        "Cols": [
            {
                "Col": "id",
                "Type": "tinyint(4) unsigned"
            },
            {
                "Col": "name",
                "Type": "varchar(16)"
            },
            {
                "Col": "short_name",
                "Type": "varchar(8)"
            },
            {
                "Col": "code",
                "Type": "varchar(256)"
            }
        ],
        "DbName": "test",
        "InstanceId": "tdsql-e9tklsgz",
        "RequestId": "2de52957-ebe4-4d7b-8985-4e415b3fb360",
        "Table": "region"
    }
}
```

