**Example 1: 拉取多个云存事件缩略图**



Input: 

```
tccli iotvideo DescribeCloudStorageMultiThumbnail --cli-unfold-argument  \
    --ProductId product \
    --DeviceName dev \
    --MultiThumbnail /100008401725/AQTV2839QJ/sp01_32820237_7/events/1615200613.jpg|/100008401725/AQTV2839QJ/sp01_32820237_7/events/1615200613.jpg
```

Output: 
```
{
    "Response": {
        "ThumbnailURLInfoList": [
            {
                "ThumbnailURL": "https",
                "ExpireTime": 0
            }
        ],
        "RequestId": "id"
    }
}
```

