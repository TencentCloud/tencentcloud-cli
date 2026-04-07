**Example 1: 主资源ID查询所有从资源列表**



Input: 

```
tccli tione DescribeResourceGroupRelativeResources --cli-unfold-argument  \
    --ResourceGroupIds rsg-wvlc6fcp
```

Output: 
```
{
    "Response": {
        "ResourceGroupRelativeResources": [
            {
                "SlaveResourceType": "trainingtask",
                "SlaveResources": [
                    {
                        "MasterResourceID": "rsg-wvlc6fcp",
                        "SlaveResourceIDs": [
                            "train-1544125357018442368"
                        ]
                    }
                ],
                "TotalCount": 2
            }
        ],
        "TotalCount": 9,
        "RequestId": "90da9a70-b8c6-4894-9abe-d08b052fc76c"
    }
}
```

**Example 2: 从资源ID查询主资源ID**



Input: 

```
tccli tione DescribeResourceGroupRelativeResources --cli-unfold-argument  \
    --Filters.0.Name ResourceType \
    --Filters.0.Values batch
```

Output: 
```
{
    "Response": {
        "ResourceGroupRelativeResources": [
            {
                "SlaveResourceType": "batch",
                "SlaveResources": [
                    {
                        "MasterResourceID": "rsg-wvlc6fcp",
                        "SlaveResourceIDs": [
                            "batch-b9q1ub55p8cg"
                        ]
                    }
                ],
                "TotalCount": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "73fec2f0-4e13-41f1-bf19-458c44551a5c"
    }
}
```

