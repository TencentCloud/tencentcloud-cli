**Example 1: 查询从实例列表**



Input: 

```
tccli tcr DescribeReplicationInstances --cli-unfold-argument  \
    --RegistryId tcr-12345 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "76e69894-670f-4440-8773-075763fbdb80",
        "TotalCount": 1,
        "ReplicationRegistries": [
            {
                "RegistryId": "tcr-06d62e1r",
                "ReplicationRegistryId": "tcr-06d62e1r-5",
                "ReplicationRegionId": 5,
                "ReplicationRegionName": "ap-hongkong",
                "Status": "Running",
                "CreatedAt": "2020-09-28T15:34:59+08:00"
            }
        ]
    }
}
```

