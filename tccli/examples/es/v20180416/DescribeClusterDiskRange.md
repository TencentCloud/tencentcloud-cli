**Example 1: demo**



Input: 

```
tccli es DescribeClusterDiskRange --cli-unfold-argument  \
    --InstanceId es-xxx
```

Output: 
```
{
    "Response": {
        "NodeTypeDiskSizeRangeList": [
            {
                "NodeType": "ES.SA2.MEDIUM4",
                "Type": "hotData",
                "Min": 1,
                "Med": 2,
                "Max": 3,
                "DiskCountMin": 1,
                "DiskCountMax": 2,
                "DiskEncrypt": 0,
                "DiskEnhance": 0,
                "IsLvm": 0,
                "IsLocalDiskType": false
            },
            {
                "NodeType": "ES.SA2.MEDIUM4",
                "Type": "warmData",
                "Min": 1,
                "Med": 2,
                "Max": 3,
                "DiskCountMin": 1,
                "DiskCountMax": 2,
                "DiskEncrypt": 0,
                "DiskEnhance": 0,
                "IsLvm": 0,
                "IsLocalDiskType": false
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

