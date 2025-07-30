**Example 1: 查询生命周期管理策略**



Input: 

```
tccli cfs DescribeLifecyclePolicies --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --LifecyclePolicyName test
```

Output: 
```
{
    "Response": {
        "PageNumber": 1,
        "PageSize": 10,
        "TotalCount": 2,
        "LifecyclePolicies": [
            {
                "CreateTime": "2022-03-01 10:38:54",
                "LifecyclePolicyID": "policy-ek8aw4id",
                "LifecyclePolicyName": "test",
                "LifecycleRules": [
                    {
                        "StorageType": "InfrequentAccess",
                        "Interval": "DEFAULT_ATIME_14",
                        "FileType": "BIG_FILE",
                        "Action": "noarchive",
                        "FileMinSize": "",
                        "FileMaxSize": "1G"
                    },
                    {
                        "StorageType": "InfrequentAccess",
                        "Interval": "DEFAULT_ATIME_14",
                        "FileType": "ALL",
                        "Action": "archive",
                        "FileMinSize": "",
                        "FileMaxSize": ""
                    }
                ],
                "Paths": [
                    {
                        "FileSystemId": "cfs-4030acd30",
                        "Path": "/data/log1/"
                    },
                    {
                        "FileSystemId": "cfs-4030acd30",
                        "Path": "/data/log2/"
                    }
                ]
            },
            {
                "CreateTime": "2022-03-02 14:27:46",
                "LifecyclePolicyID": "policy-phpizowr",
                "LifecyclePolicyName": "test-jay",
                "LifecycleRules": [
                    {
                        "StorageType": "InfrequentAccess",
                        "Interval": "DEFAULT_ATIME_14",
                        "FileType": "BIG_FILE",
                        "Action": "noarchive",
                        "FileMinSize": "",
                        "FileMaxSize": "1G"
                    },
                    {
                        "StorageType": "InfrequentAccess",
                        "Interval": "DEFAULT_ATIME_14",
                        "FileType": "ALL",
                        "Action": "archive",
                        "FileMinSize": "",
                        "FileMaxSize": ""
                    }
                ],
                "Paths": []
            }
        ],
        "RequestId": "aaaa-bbbb-cccc-eeeee"
    }
}
```

