**Example 1: 查询当前存储情况**

查询当前存储情况

Input: 

```
tccli vod DescribeStorageData --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "MediaCount": 100,
        "TotalStorage": 4700000,
        "InfrequentStorage": 0,
        "StandardStorage": 2000000,
        "ArchiveStorage": 1500000,
        "DeepArchiveStorage": 1200000,
        "StorageStat": [
            {
                "Area": "Chinese Mainland",
                "TotalStorage": 3800000,
                "InfrequentStorage": 0,
                "StandardStorage": 1800000,
                "ArchiveStorage": 1000000,
                "DeepArchiveStorage": 1000000
            },
            {
                "Area": "Outside Chinese Mainland",
                "TotalStorage": 900000,
                "InfrequentStorage": 0,
                "StandardStorage": 200000,
                "ArchiveStorage": 500000,
                "DeepArchiveStorage": 200000
            }
        ],
        "RequestId": "12345678-90ab-cdef-1234-567890abcdef"
    }
}
```

