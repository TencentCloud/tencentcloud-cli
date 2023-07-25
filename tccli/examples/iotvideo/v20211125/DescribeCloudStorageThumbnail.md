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
        "ThumbnailURL": "https://video-cv-1258344699.cos.ap-guangzhou.myqcloud.com/%2F100008401725%2FAQTV2839QJ%2Fsp01_32820237_5%2Fevents%2F1614908216.jpg?q-sign-algorithm=sha1&q-ak=AKIDAbqpXyZb6KJ6dtvwkRwAqLbfNvIZlYJp&q-sign-time=1614909378%3B1614912978&q-key-time=1614909378%3B1614912978&q-header-list=host&q-url-param-list=&q-signature=59cfa8d69bb77980ba757cb111de62fc6c4880f5",
        "ExpireTime": 1
    }
}
```

