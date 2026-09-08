**Example 1: 查询图谱下所有接入任务**



Input: 

```
tccli cls DescribeResourceGraphProductIngestTaskList --cli-unfold-argument  \
    --ResourceGraphId 649f38d6-3fe9-4412-a31c-ddb701f9e5a9
```

Output: 
```
{
    "Response": {
        "ProductIngestTaskItems": [
            {
                "CreateTime": 1783324318,
                "Name": "产品接入任务-test-15",
                "Product": "tke",
                "Status": 1,
                "TaskId": "eff846ca-d6f2-42bc-8578-3579b8c0c356",
                "UpdateTime": 1783324323
            }
        ],
        "TotalCount": 7,
        "RequestId": "490bf849-f99f-4a41-a612-4766b789b4ec"
    }
}
```

