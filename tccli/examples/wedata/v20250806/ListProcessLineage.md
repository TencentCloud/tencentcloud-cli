**Example 1: 查询任务血缘**



Input: 

```
tccli wedata ListProcessLineage --cli-unfold-argument  \
    --ProcessId 110111121 \
    --ProcessType SCHEDULE_TASK \
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
                    "Source": {
                        "CreateTime": "2025-09-04 20:05:20",
                        "Description": "HIVE",
                        "LineageNodeId": "pNevFHwaLuad0dJvnUtYGQ",
                        "Platform": "WEDATA",
                        "ResourceName": "source",
                        "ResourceProperties": null,
                        "ResourceType": "TABLE",
                        "ResourceUniqueId": "qwerty",
                        "UpdateTime": "2025-09-04 20:32:37"
                    },
                    "Target": {
                        "CreateTime": "2025-09-04 20:19:39",
                        "Description": null,
                        "LineageNodeId": "Dk7f8Z4OzgC-AjjPb5XbwA",
                        "Platform": "WEDATA",
                        "ResourceName": "target",
                        "ResourceProperties": null,
                        "ResourceType": "TABLE",
                        "ResourceUniqueId": "qwerty1",
                        "UpdateTime": "2025-09-04 20:32:37"
                    }
                },
                {
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
                    "Source": {
                        "CreateTime": "2025-10-10 11:38:30",
                        "Description": "HIVE",
                        "LineageNodeId": "C6rFORILOlc9iRK9xO-tDA",
                        "Platform": "WEDATA",
                        "ResourceName": "source",
                        "ResourceProperties": null,
                        "ResourceType": "TABLE",
                        "ResourceUniqueId": "xxxx-xxxx-xxxx-xxxx",
                        "UpdateTime": "2025-10-10 11:38:30"
                    },
                    "Target": {
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
            "TotalCount": 2
        },
        "RequestId": "92a6a0e1-823f-460e-a5ce-cb8f72cfa79a"
    }
}
```

