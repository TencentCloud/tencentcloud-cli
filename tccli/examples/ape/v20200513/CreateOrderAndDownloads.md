**Example 1: 核销图片，获取图片URL地址**



Input: 

```
tccli ape CreateOrderAndDownloads --cli-unfold-argument  \
    --ImageInfos.0.ImageId 10561576 \
    --ImageInfos.0.DimensionsNameId 8 \
    --ImageInfos.0.LicenseScopeId 8
```

Output: 
```
{
    "Response": {
        "DownloadInfos": [
            {
                "ConsumeType": 2,
                "DownloadId": "apid-9hy8xxxf",
                "DownloadTime": "2021-01-29 14:46:57",
                "FirstDownload": true,
                "ImageInfo": {
                    "DimensionsNameId": 8,
                    "ImageId": 10561576,
                    "LicenseScopeId": 8
                },
                "ImageThumbUrl": "https://xxx/ewxx_hdd_2/114xx099/52xx0275/sxx024.jpg?imagexxxogr2/thumbnail/300x300/intxxx",
                "ImageUrl": "https://xxx/ewxx_hdd_2/114xx099/52xx0275/sxx024.jpg",
                "OrderCreateTime": "2021-01-29 14:46:57",
                "OrderId": "apod-dc7x7rxxb"
            }
        ],
        "RequestId": "s1611902815147410973",
        "TotalCount": 1
    }
}
```

