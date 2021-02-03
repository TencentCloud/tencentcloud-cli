**Example 1: 查询下载记录**



Input: 

```
tccli ape DescribeDownloadInfos --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "DownloadInfos": [
            {
                "ConsumeType": 2,
                "DownloadId": "apid-d7snj9td",
                "DownloadTime": "2021-01-29 14:59:27",
                "FirstDownload": false,
                "ImageInfo": {
                    "DimensionsNameId": 1,
                    "ImageId": 6426362,
                    "LicenseScopeId": 8
                },
                "ImageThumbUrl": "https://xxx/ewxx_hdd_2/114xx099/52xx0275/sxx024.jpg?imagexxxogr2/thumbnail/300x300/intx",
                "ImageUrl": "https://xxx/ewxx_hdd_2/114xx099/52xx0275/sxx024.jpg",
                "OrderCreateTime": "2021-01-29 14:59:06",
                "OrderId": "apod-aifit41f"
            },
            {
                "ConsumeType": 2,
                "DownloadId": "apid-i5twyeid",
                "DownloadTime": "2021-01-29 14:59:01",
                "FirstDownload": false,
                "ImageInfo": {
                    "DimensionsNameId": 1,
                    "ImageId": 3246748,
                    "LicenseScopeId": 8
                },
                "ImageThumbUrl": "https://xxx/ewxx_hdd_2/114xx099/52xx0275/sxx024.jpg?imagexxxogr2/thumbnail/300x300/intx",
                "ImageUrl": "https://xxx/ewxx_hdd_2/114xx099/52xx0275/sxx024.jpg",
                "OrderCreateTime": "2021-01-29 14:58:58",
                "OrderId": "apod-5h58gss9"
            }
        ],
        "RequestId": "s1611903576502809482",
        "TotalCount": 14
    }
}
```

