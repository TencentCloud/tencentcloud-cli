**Example 1: 将快照从广州复制到北京**

将快照从广州复制到北京

Input: 

```
tccli cbs CopySnapshotCrossRegions --cli-unfold-argument  \
    --SnapshotId snap-ckgjwkqh \
    --DestinationRegions ap-beijing
```

Output: 
```
{
    "Response": {
        "SnapshotCopyResultSet": [
            {
                "SnapshotId": "snap-d012rm6t",
                "DestinationRegion": "ap-beijing",
                "Code": "Success",
                "Message": ""
            }
        ],
        "RequestId": "98f0b5f0-7d84-4d11-9819-ee7804e524a4"
    }
}
```

