**Example 1: 批量拉取云存事件缩略图**

批量拉取云存事件缩略图

Input: 

```
tccli iotexplorer DescribeCloudStorageThumbnailList --cli-unfold-argument  \
    --ProductId H541SOP191 \
    --DeviceName event_36502632_1 \
    --ThumbnailList /100008401725/AQTV2839QJ/sp01_32820237_7/events/1615200613.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "77dbf0ae-bdee-4b09-a5eb-0086d0164a20",
        "ThumbnailURLInfoList": [
            {
                "ExpireTime": 12321321,
                "ThumbnailURL": "https://video-cv-1258344699.cos.ap-guangzhou.myqcloud.com/%2F100"
            }
        ]
    }
}
```

