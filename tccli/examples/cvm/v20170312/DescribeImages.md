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
                "LicenseType": "TencentCloud",
                "ImageId": "img-9qabwvbn",
                "OsName": "CentOS 7.6 64位",
                "ImageSize": 50,
                "ImageType": "PUBLIC_IMAGE",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "ImageState": "NORMAL",
                "ImageSource": "OFFICIAL",
                "ImageName": "CentOS 7.6 64位",
                "ImageDescription": "CentOS 7.6 64位",
                "ImageCreator": "tencent",
                "SyncPercent": 20,
                "IsSupportCloudinit": true,
                "Platform": "CentOS",
                "Architecture": "x86_64",
                "SnapshotSet": [],
                "Tags": [
                    {
                        "Key": "myKey",
                        "Value": "myValue"
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
    --Filters.0.Name image-type \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 408,
        "ImageSet": [
            {
                "LicenseType": "TencentCloud",
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
                "SyncPercent": 20,
                "SnapshotSet": [
                    {
                        "SnapshotId": "snap-gqa37j2p",
                        "DiskUsage": "SYSTEM_DISK",
                        "DiskSize": 20
                    }
                ],
                "Tags": [
                    {
                        "Key": "myKey",
                        "Value": "myValue"
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

**Example 3: 查询本地专用集群CDC的镜像缓存列表**

查询本地专用集群CDC的镜像缓存列表, 对于cdc-cache-status 可选的参数为CACHED_ALL（全部状态）、CACHING（缓存中）、CACHED（已缓存）、CACHE_INVALID（缓存失效）和 CACHE_FAILED（缓存失败）

Input: 

```
tccli cvm DescribeImages --cli-unfold-argument  \
    --Filters.0.Name dedicated-cluster-id \
    --Filters.0.Values cluster-12345678 \
    --Filters.1.Name cdc-cache-status \
    --Filters.1.Values CACHED_ALL
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ImageSet": [
            {
                "LicenseType": "TencentCloud",
                "ImageId": "img-9qabwvbn",
                "OsName": "CentOS 7.6 64位",
                "ImageSize": 50,
                "ImageType": "PUBLIC_IMAGE",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "ImageState": "NORMAL",
                "ImageSource": "OFFICIAL",
                "ImageName": "CentOS 7.6 64位",
                "ImageDescription": "CentOS 7.6 64位",
                "ImageCreator": "tencent",
                "SyncPercent": 20,
                "IsSupportCloudinit": true,
                "Platform": "CentOS",
                "Architecture": "x86_64",
                "SnapshotSet": [],
                "Tags": [
                    {
                        "Key": "myKey",
                        "Value": "myValue"
                    }
                ],
                "CdcCacheStatus": "CACHED"
            }
        ],
        "RequestId": "8b56af0b-f8ec-401e-9b80-30767ae4d432"
    }
}
```

