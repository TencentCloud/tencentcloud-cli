**Example 1: 对象存储异常检测调用记录信息**



Input: 

```
tccli csip DescribeIpInvokeRecord --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "6a625df7-dea0-4ba2-9942-97303d13d23e",
        "Data": [
            {
                "AkName": "AKID0987654321fedcba",
                "AkMark": "生产AK",
                "InvokeWay": "API",
                "RelBucket": {
                    "AppId": 21432134,
                    "BucketName": "prod-bucket"
                },
                "InvokeAction": "PutObject",
                "InvokeFileName": "upload/data.json",
                "InvokeCount": 3,
                "InvokeStatus": "Success",
                "RelCamCount": 1,
                "LastAccessTime": 1705296000,
                "RelAssetName": "",
                "RelAssetId": "",
                "SourceIpType": 1,
                "UA": "cos-console",
                "SourceIp": "",
                "FirstAccessTime": 1,
                "SourceIpISP": "移动"
            }
        ],
        "Total": 2
    }
}
```

