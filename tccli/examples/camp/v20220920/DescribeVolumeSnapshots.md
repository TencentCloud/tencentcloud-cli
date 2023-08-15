**Example 1: 获取卷快照列表**



Input: 

```
tccli camp DescribeVolumeSnapshots --cli-unfold-argument  \
    --ProjectID abc \
    --EnvironmentName abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.Op abc \
    --Filters.0.Query abc \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "VolumeSnapshots": [
            {
                "Name": "vs-1",
                "ClusterID": "cls-mg7ol3cm",
                "PersistentVolumeClaimName": "pvc-1",
                "ReadyToUse": false,
                "BoundVolumeSnapshotContentName": "content-1",
                "VolumeSnapshotContent": {
                    "Name": "content-1",
                    "ReadyToUse": true,
                    "SnapshotHandle": "snap-abc",
                    "RestoreSize": 222
                }
            },
            {
                "Name": "vs-2",
                "ClusterID": "cls-mg7ol3cm",
                "PersistentVolumeClaimName": "pvc-2",
                "ReadyToUse": false,
                "BoundVolumeSnapshotContentName": "",
                "VolumeSnapshotContent": null
            }
        ],
        "RequestId": "abc"
    }
}
```

