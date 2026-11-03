**Example 1: 查询CFS文件系统和COS Bucket列表**



Input: 

```
tccli dlc ListStorages --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CFSFileSystems": [
            {
                "FileSystemId": "cfs-c2ggthgx"
            }
        ],
        "COSBuckets": [
            {
                "Name": "turkey-cos-260090589"
            }
        ],
        "RequestId": "9dad3c0f-5f73-4f83-9bba-b39a3abfebaf"
    }
}
```

