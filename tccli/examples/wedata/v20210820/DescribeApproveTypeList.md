**Example 1: 测试通过示例**



Input: 

```
tccli wedata DescribeApproveTypeList --cli-unfold-argument  \
    --Classification db
```

Output: 
```
{
    "Response": {
        "RequestId": "d4fe8fc5-ceb2-47fe-be21-8e5be39e28f1",
        "Data": [
            {
                "Type": "db_db",
                "TypeName": "库申请",
                "Classification": "db"
            },
            {
                "Type": "db_table",
                "TypeName": "表申请",
                "Classification": "db"
            }
        ]
    }
}
```

