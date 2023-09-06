**Example 1: 添加查询云应用状态请求**



Input: 

```
tccli car DescribeApplicationStatus --cli-unfold-argument  \
    --ApplicationIdList app-lgefeha
```

Output: 
```
{
    "Response": {
        "StatusList": [
            {
                "ApplicationId": "app-lgefeha",
                "ApplicationRunStatus": "ApplicationRunning",
                "ApplicationUpdateStatus": "ApplicationUpdateNormal",
                "ApplicationUpdateProgress": 100
            }
        ],
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022"
    }
}
```

