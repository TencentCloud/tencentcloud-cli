**Example 1: 按镜像ID查询镜像**

已经知道镜像ID，查询镜像相关信息。

Input: 

```
tccli cvm DescribeImages --cli-unfold-argument  \
    --Filters.0.Values img-9qabwvbn \
    --Filters.0.Name image-id
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ImageSet": [
            {
                "ImageId": "img-9qabwvbn",
                "OsName": "CentOS 7.6 64位",
                "ImageSize": 50,
                "ImageType": "PUBLIC_IMAGE",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "ImageState": "NORMAL",
                "ImageSource": "OFFICIAL",
                "ImageName": "CentOS 7.6 64位",
                "ImageDescription": "CentOS 7.6 64位",
                "ImageCreator": null,
                "SyncPercent": null,
                "IsSupportCloudinit": true,
                "Platform": "CentOS",
                "Architecture": "x86_64",
                "SnapshotSet": [],
                "Tags": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ]
            }
        ],
        "RequestId": "db145873-3128-4079-8cec-65e05a7c9f89"
    }
}
```

**Example 2: 按镜像类型查询镜像**

查询账户下所有私有镜像。

Input: 

```
tccli cvm DescribeImages --cli-unfold-argument  \
    --Filters.0.Values PRIVATE_IMAGE \
    --Filters.0.Name image-type
```

Output: 
```
{
    "Response": {
        "TotalCount": 408,
        "ImageSet": [
            {
                "OsName": "CentOS 7.4 64位",
                "ImageSize": 20,
                "ImageType": "PRIVATE_IMAGE",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "ImageDescription": "test-image",
                "ImageSource": "CREATE_IMAGE",
                "ImageId": "img-qlzp4oea",
                "ImageName": "test-image",
                "ImageCreator": "3205597606",
                "ImageState": "NORMAL",
                "SyncPercent": null,
                "SnapshotSet": [
                    {
                        "SnapshotId": "snap-gqa37j2p",
                        "DiskUsage": "SYSTEM_DISK",
                        "DiskSize": 20
                    }
                ],
                "Tags": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "Architecture": "x86_64",
                "Platform": "CentOS",
                "IsSupportCloudinit": true
            }
        ],
        "RequestId": "5908394c-5b3f-42e0-a537-8410553890a5"
    }
}
```

