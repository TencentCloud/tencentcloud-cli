**Example 1: 查询实例的表对象**



Input: 

```
tccli mariadb DescribeDatabaseObjects --cli-unfold-argument  \
    --InstanceId tdsql-e9tklsgz \
    --DbName test
```

Output: 
```
{
    "Response": {
        "DbName": "test",
        "Funcs": [],
        "InstanceId": "tdsql-e9tklsgz",
        "Procs": [
            {
                "Proc": "AddGeometryColumn"
            },
            {
                "Proc": "DropGeometryColumn"
            }
        ],
        "RequestId": "a70c33e5-0c38-43a0-9953-234accd84d2a",
        "Tables": [
            {
                "Table": "region"
            }
        ],
        "Views": []
    }
}
```

