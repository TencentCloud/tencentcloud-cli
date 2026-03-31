**Example 1: 获取适合的自动镜像缓存**



Input: 

```
tccli tke GetMostSuitableImageCache --cli-unfold-argument  \
    --Images redis:8.6.1-trixie
```

Output: 
```
{
    "Response": {
        "Found": true,
        "ImageCache": {
            "CreationTime": "2026-03-30 07:03:35 +0000 UTC",
            "Events": [
                {
                    "FirstTimestamp": "2026-03-30 07:03:45 +0000 UTC",
                    "ImageCacheId": "imc-r1htp8tg",
                    "LastTimestamp": "2026-03-30 07:03:45 +0000 UTC",
                    "Message": "create disk disk-320438xa successfully",
                    "Reason": "DiskCreated",
                    "Type": "Normal"
                }
            ],
            "ExpireDateTime": "2126-03-30 07:03:35 +0000 UTC",
            "ImageCacheId": "imc-r1htp8tg",
            "ImageCacheName": "munaltest2",
            "ImageCacheSize": 20,
            "ImageCacheType": "manual",
            "ImageRegistryCredentials": [],
            "Images": [
                "redis:8.6.1-trixie"
            ],
            "LastMatchedTime": "2026-03-30 17:07:11.389402882 +0800 CST m=+893.262707991",
            "RetentionDays": 0,
            "SnapshotId": "snap-fji6ytcl",
            "Snapshotter": "overlay",
            "Status": "Ready",
            "Tags": []
        },
        "RequestId": "d981508f-969e-449d-a0ba-8cc4193c33ac"
    }
}
```

