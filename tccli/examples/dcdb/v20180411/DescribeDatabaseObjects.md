**Example 1: 查询数据库对象信息**



Input: 

```
tccli dcdb DescribeDatabaseObjects --cli-unfold-argument  \
    --InstanceId dcdbt-52s53yyh \
    --DbName test
```

Output: 
```
{
    "Response": {
        "RequestId": "742443a5-4683-48ba-b30e-5151d26cf62d",
        "InstanceId": "dcdbt-52s53yyh",
        "DbName": "test",
        "Tables": [],
        "Views": [],
        "Procs": [
            {
                "Proc": "AddGeometryColumn"
            },
            {
                "Proc": "DropGeometryColumn"
            }
        ],
        "Funcs": []
    }
}
```

