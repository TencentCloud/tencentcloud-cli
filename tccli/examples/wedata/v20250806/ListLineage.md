**Example 1: 查询血缘**



Input: 

```
tccli wedata ListLineage --cli-unfold-argument  \
    --ResourceUniqueId xxxx-xxxx-xxxx-xxxx \
    --ResourceType TABLE \
    --Direction OUTPUT \
    --PageNumber 1 \
    --PageSize 10 \
    --Platform WEDATA
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Relation": {
                        "Processes": [
                            {
                                "LineageNodeId": "SDb_53ltpnfnIxb7dNQQRA",
                                "Platform": "WEDATA",
                                "ProcessId": "110111121",
                                "ProcessProperties": null,
                                "ProcessSubType": null,
                                "ProcessType": "THIRD_REPORT"
                            }
                        ],
                        "RelationId": "C6rFORILOlc9iRK9xO-tDA::j4maUgkJhZ7gYm7WvRbOEQ",
                        "SourceUniqueId": "C6rFORILOlc9iRK9xO-tDA",
                        "TargetUniqueId": "j4maUgkJhZ7gYm7WvRbOEQ"
                    },
                    "Resource": {
                        "CreateTime": "2025-10-10 11:38:30",
                        "Description": "MYSQL",
                        "LineageNodeId": "j4maUgkJhZ7gYm7WvRbOEQ",
                        "Platform": "WEDATA",
                        "ResourceName": "target",
                        "ResourceProperties": null,
                        "ResourceType": "TABLE",
                        "ResourceUniqueId": "xxxx-xxxx-xxxx-xxxx1",
                        "UpdateTime": "2025-10-10 11:38:30"
                    }
                }
            ],
            "PageCount": 1,
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1
        },
        "RequestId": "ab403c56-b05f-466a-80bc-000aa767ba1d"
    }
}
```

