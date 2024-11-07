**Example 1: 拉取云存事件缩略图**



Input: 

```
tccli iotvideo DescribeCloudStorageThumbnail --cli-unfold-argument  \
    --ProductId AQTV2839QJ \
    --DeviceName sp01_32820237_5 \
    --Thumbnail /100008401725/AQTV2839QJ/sp01_32820237_7/events/1615200613.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "c299d2c9-805f-41a5-853d-db32ba1a16b5",
        "ThumbnailURL": "*************",
        "ExpireTime": 1
    }
}
```

