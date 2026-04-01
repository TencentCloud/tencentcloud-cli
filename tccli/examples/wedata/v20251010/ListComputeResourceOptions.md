**Example 1: 查询计算资源列表：下拉框**



Input: 

```
tccli wedata ListComputeResourceOptions --cli-unfold-argument  \
    --WorkspaceId 12 \
    --Page.PageSize 10 \
    --Page.PageNumber 1 \
    --ResourceTypes None
```

Output: 
```
{
    "Response": {
        "Data": {
            "Resources": [
                {
                    "AvailableCU": 80,
                    "BasicInfo": {
                        "ResourceId": "mock_resource_001",
                        "ResourceName": "Mock Resource 1",
                        "ResourceStatus": 3,
                        "ResourceType": 2
                    },
                    "TotalCU": 100
                },
                {
                    "BasicInfo": {
                        "ResourceId": "mock_resource_002",
                        "ResourceName": "Mock Resource 2",
                        "ResourceStatus": 4,
                        "ResourceType": 1
                    },
                    "TotalCU": 50
                }
            ]
        },
        "RequestId": "c4d0ce7e-226a-48c2-99cf-d71d6b15f78d"
    }
}
```

