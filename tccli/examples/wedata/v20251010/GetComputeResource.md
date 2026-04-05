**Example 1: 获取计算资源详情信息**



Input: 

```
tccli wedata GetComputeResource --cli-unfold-argument  \
    --ResourceId 12
```

Output: 
```
{
    "Response": {
        "Data": {
            "BasicInfo": {
                "ResourceId": "12",
                "ResourceName": "Mock Compute Resource",
                "ResourceStatus": 3,
                "ResourceType": 2
            },
            "BillType": "postpaid",
            "Creator": "mock_user_001",
            "Description": "This is a mock compute resource for testing",
            "ResourceConfig": {
                "AutoStartStop": true,
                "AutoStopSeconds": 3600,
                "MaxCU": 100,
                "MaxConcurrency": 5,
                "MaxInstances": 10,
                "MinCU": 10,
                "SingleInstanceQuota": 10
            },
            "UpdateTime": "1764818911937"
        },
        "RequestId": "ce0e571a-b7a7-4ba8-b942-923374ff5b3f"
    }
}
```

