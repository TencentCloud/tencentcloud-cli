**Example 1: 获取数据库信息**

获取internal数据源的库信息

Input: 

```
tccli cdwdoris DescribeDatabase --cli-unfold-argument  \
    --InstanceId cdwdoris-bjizjxxx \
    --CatalogName internal
```

Output: 
```
{
    "Response": {
        "DbInfos": [
            {
                "DbName": "db1",
                "Location": "",
                "Properties": []
            }
        ],
        "Message": "",
        "RequestId": "43516a7e-aa6c-4f43-8435-71d4e41dbd8a"
    }
}
```

