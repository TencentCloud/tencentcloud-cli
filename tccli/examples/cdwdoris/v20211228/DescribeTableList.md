**Example 1: 获取表列表**

获取internal数据源和demo库下的表列表

Input: 

```
tccli cdwdoris DescribeTableList --cli-unfold-argument  \
    --InstanceId cdwdoris-bjizjxxx \
    --DbName demo
```

Output: 
```
{
    "Response": {
        "Message": "",
        "RequestId": "28caf1f1-9192-477c-94d4-e910b87ca0fc",
        "TableNames": [
            "add_table2",
            "table"
        ]
    }
}
```

