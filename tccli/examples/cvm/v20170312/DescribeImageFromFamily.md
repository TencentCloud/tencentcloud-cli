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
            "ImageId": "img-1a2b3c4d",
            "OsName": "Ubuntu Server 20.04 LTS 64bit",
            "ImageType": "PRIVATE_IMAGE",
            "CreatedTime": "2025-03-24T06:35:06Z",
            "ImageName": "myImg",
            "ImageDescription": "myImg",
            "ImageSize": 50,
            "Architecture": "x86_64",
            "ImageState": "NORMAL",
            "Platform": "Ubuntu",
            "ImageCreator": "tencent",
            "ImageSource": "CREATE_IMAGE",
            "SyncPercent": 0,
            "IsSupportCloudinit": true,
            "SnapshotSet": [
                {
                    "SnapshotId": "snap-1a2b3c4d",
                    "DiskUsage": "SYSTEM_DISK",
                    "DiskSize": 50
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

