**Example 1: 查看镜像族列表**



Input: 

```
tccli cvm DescribeImageFromFamily --cli-unfold-argument  \
    --ImageFamily business-daily-update
```

Output: 
```
{
    "Response": {
        "Image": {
            "ImageId": "abc",
            "OsName": "abc",
            "ImageType": "abc",
            "CreatedTime": "2020-09-22T00:00:00+00:00",
            "ImageName": "abc",
            "ImageDescription": "abc",
            "ImageSize": 0,
            "Architecture": "abc",
            "ImageState": "abc",
            "Platform": "abc",
            "ImageCreator": "abc",
            "ImageSource": "abc",
            "SyncPercent": 0,
            "IsSupportCloudinit": true,
            "SnapshotSet": [
                {
                    "SnapshotId": "abc",
                    "DiskUsage": "abc",
                    "DiskSize": 0
                }
            ],
            "Tags": [
                {
                    "Key": "abc",
                    "Value": "abc"
                }
            ],
            "LicenseType": "abc",
            "ImageFamily": "business-daily-update",
            "ImageDeprecated": false
        },
        "RequestId": "5908394c-5b3f-42e0-a537-8410553890a5"
    }
}
```

