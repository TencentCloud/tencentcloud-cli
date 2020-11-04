**Example 1: 查询实例的库列表**



Input: 

```
tccli mariadb DescribeDatabases --cli-unfold-argument  \
    --InstanceId tdsql-e9tklsgz
```

Output: 
```
{
    "Response": {
        "Databases": [
            {
                "DbName": "information_schema"
            },
            {
                "DbName": "mysql"
            },
            {
                "DbName": "performance_schema"
            },
            {
                "DbName": "test"
            }
        ],
        "InstanceId": "tdsql-e9tklsgz",
        "RequestId": "86cb12ed-0e1f-416c-99a6-79f83a8fd31e"
    }
}
```

