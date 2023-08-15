**Example 1: 获取卷快照详情**



Input: 

```
tccli camp DescribeVolumeSnapshot --cli-unfold-argument  \
    --ProjectID abc \
    --EnvironmentName abc \
    --ClusterID abc \
    --Name abc
```

Output: 
```
{
    "Response": {
        "VolumeSnapshot": {
            "Name": "fox-snap-3",
            "PersistentVolumeClaimName": "ngx2-test-ngx2-0",
            "ReadyToUse": true,
            "VolumeSnapshotContent": {
                "Name": "snapcontent-bde9b448-b145-4448-94c3-3b0a02d06814",
                "SnapshotHandle": "snap-khu03bjz",
                "RestoreSize": 10737418240,
                "ReadyToUse": true
            }
        },
        "RequestId": "abc"
    }
}
```

