**Example 1: 配置生命周期策略关联目录**



Input: 

```
tccli cfs ApplyPathLifecyclePolicy --cli-unfold-argument  \
    --LifecyclePolicyID policy-ek8aw4id \
    --Paths.0.FileSystemId cfs-4030acd30 \
    --Paths.0.Path /data
```

Output: 
```
{
    "Response": {
        "CheckResults": [
            {
                "LifecyclePolicyID": "policy-4cqyxcma",
                "FileSystemId": "cfs-5ajk45jk8",
                "Path": "/data/home/user00/",
                "LifecycleRules": [
                    {
                        "StorageType": "InfrequentAccess",
                        "Interval": "DEFAULT_ATIME_14",
                        "FileType": "All",
                        "Action": "Archive",
                        "FileMaxSize": "1G",
                        "FileMinSize": "1M"
                    }
                ],
                "TargetPath": "/data/home/user00/"
            }
        ],
        "RequestId": "a1b2c3-d4e5f6-g7h8j9"
    }
}
```

