**Example 1: 查询连通性检测任务结果**

查询连通性检测任务结果

Input: 

```
tccli dbs DescribeConnectTestResult --cli-unfold-argument  \
    --TaskIds 123
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Addr": "",
                "IsPass": 0,
                "SNatIp": "",
                "Status": "",
                "TaskId": 0,
                "TestItems": []
            }
        ],
        "TotalCount": 0,
        "RequestId": "cf6db42c-0eed-4aaf-a8aa-0b2e21e09573"
    }
}
```

