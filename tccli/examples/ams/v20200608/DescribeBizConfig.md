**Example 1: 查看单个配置**

查看单个配置

Input: 

```
tccli ams DescribeBizConfig --cli-unfold-argument  \
    --BizType 1001
```

Output: 
```
{
    "Response": {
        "BizType": "1001",
        "BizName": "测试项目",
        "ModerationCategories": [
            "Porn"
        ],
        "MediaModeration": {
            "ImageFrequency": 1,
            "AudioFrequency": 60,
            "UseOCR": false,
            "UseAudio": true,
            "CallbackUrl": "http://example.com/fromcms",
            "SegmentOutput": {
                "Bucket": "cms-256309736",
                "Region": "ap-guangzhou",
                "ObjectPrefix": "_cms_segments/"
            }
        },
        "CreatedAt": "2020-07-13T11:46:43.840Z",
        "UpdatedAt": "2020-07-13T11:46:43.840Z",
        "RequestId": "8d3e4765-48db-40b5-8fdb-aaf1d7225a60"
    }
}
```

