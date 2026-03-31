**Example 1: 获取计算资源列表**



Input: 

```
tccli wedata ListComputeResources --cli-unfold-argument  \
    --WorkspaceId 12 \
    --ResourceTypes None \
    --ResourceStatuses None \
    --Keywords None \
    --Page.PageNumber 1 \
    --Page.PageSize 10 \
    --CreatorIds None \
    --OrderFields.0.Name None \
    --OrderFields.0.Direction None
```

Output: 
```
{
    "Response": {
        "Data": {
            "Page": {
                "TotalCount": 2
            },
            "Resources": [
                {
                    "AutoStopSeconds": "3600",
                    "BasicInfo": {
                        "ResourceId": "mock_resource_001",
                        "ResourceName": "Mock Resource 1",
                        "ResourceStatus": 3,
                        "ResourceType": 2
                    },
                    "BillType": "postpaid",
                    "CUQuota": 100,
                    "CreateTime": "1762227124727",
                    "Creator": "mock_user_001",
                    "ExpirationTime": "1796355124727",
                    "Operations": [
                        1,
                        2,
                        3
                    ],
                    "UpdateTime": "1764819124727"
                },
                {
                    "AutoStopSeconds": "1800",
                    "BasicInfo": {
                        "ResourceId": "mock_resource_002",
                        "ResourceName": "Mock Resource 2",
                        "ResourceStatus": 4,
                        "ResourceType": 1
                    },
                    "BillType": "postpaid",
                    "CUQuota": 50,
                    "CreateTime": "1759548724727",
                    "Creator": "mock_user_002",
                    "ExpirationTime": "1796355124727",
                    "Operations": [
                        1,
                        2,
                        3
                    ],
                    "UpdateTime": "1762227124727"
                }
            ]
        },
        "RequestId": "20974448-bb82-4760-9c02-2196cfc8bbe2"
    }
}
```

