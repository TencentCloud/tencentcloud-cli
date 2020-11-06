**Example 1: DescribeOtaVersions**



Input: 

```
tccli iotvideo DescribeOtaVersions --cli-unfold-argument  \
    --ProductId 123456789000 \
    --OtaVersion ** \
    --PubStatus 1 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Data": [
            {
                "PubStatus": 1,
                "Remark": "xx",
                "GrayValue": 1,
                "Tids": "xx",
                "OldVersions": "xx",
                "OtaVersion": "xx",
                "UpdateTime": 1,
                "PublishTime": 1,
                "ActiveCount": 0,
                "OnlineCount": 0,
                "FileSize": 1,
                "UploadTime": 1,
                "ProductId": "xx",
                "ModifyTimes": 1,
                "VersionUrl": "xx",
                "Contents": {
                    "En": "xx",
                    "Cn": "xx",
                    "Tc": "xx"
                },
                "Md5": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

