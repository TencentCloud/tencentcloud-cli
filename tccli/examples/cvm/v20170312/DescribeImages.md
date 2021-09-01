**Example 1: 按镜像ID查询镜像**

已经知道镜像ID，查询镜像相关信息。

Input: 

```
tccli cvm DescribeImages --cli-unfold-argument  \
    --Filters.0.Name image-id \
    --Filters.0.Values img-9qabwvbn
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
                "ImageSize": 10,
                "ImageType": "PUBLIC_IMAGE",
                "CreatedTime": null,
                "ImageState": "NORMAL",
                "ImageSource": "OFFICIAL",
                "ImageName": "CentOS 7.6 64位",
                "ImageDescription": "CentOS 7.6 64位",
                "ImageCreator": null,
                "SyncPercent": null,
                "IsSupportCloudinit": true,
                "Platform": "CentOS",
                "Architecture": "x86_64",
                "SnapshotSet": []
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
    --Filters.0.Name image-type \
    --Filters.0.Values PRIVATE_IMAGE
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
                "CreatedTime": "2021-03-10T03:28:10Z",
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
                "Architecture": "x86_64",
                "Platform": "CentOS",
                "IsSupportCloudinit": true
            }
        ],
        "RequestId": "5908394c-5b3f-42e0-a537-8410553890a5"
    }
}
```

