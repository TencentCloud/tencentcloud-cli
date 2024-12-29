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
            "ImageId": "img-xxx",
            "OsName": "Xserver",
            "ImageType": "PRIVATE_IMAGE",
            "CreatedTime": "2020-09-22T00:00:00+00:00",
            "ImageName": "myImg",
            "ImageDescription": "",
            "ImageSize": 0,
            "Architecture": "x86_64",
            "ImageState": "NORMAL",
            "Platform": "Windows",
            "ImageCreator": "tencent",
            "ImageSource": "CREATE_IMAGE",
            "SyncPercent": 0,
            "IsSupportCloudinit": true,
            "SnapshotSet": [
                {
                    "SnapshotId": "snap-nbxxx56",
                    "DiskUsage": "SYSTEM_DISK",
                    "DiskSize": 0
                }
            ],
            "Tags": [
                {
                    "Key": "myKey",
                    "Value": "myValue"
                }
            ],
            "LicenseType": "TencentCloud",
            "ImageFamily": "business-daily-update",
            "ImageDeprecated": false
        },
        "RequestId": "5908394c-5b3f-42e0-a537-8410553890a5"
    }
}
```

