**Example 1: 查询当前存储情况**



Input: 

```
tccli vod DescribeStorageData --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "MediaCount": 0,
        "TotalStorage": 2000000,
        "InfrequentStorage": 0,
        "StandardStorage": 2000000,
        "StorageStat": [
            {
                "Area": "Chinese Mainland",
                "TotalStorage": 1800000,
                "InfrequentStorage": 0,
                "StandardStorage": 1800000
            },
            {
                "Area": "outside Chinese Mainland",
                "TotalStorage": 200000,
                "InfrequentStorage": 0,
                "StandardStorage": 200000
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287s3"
    }
}
```

