**Example 1: 获取应为类分分组列表**



Input: 

```
tccli tencentcloudintl DescribeCategoryGroupByLang --cli-unfold-argument  \
    --Lang en
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Children": [],
                "GroupId": 14,
                "IconHoverUrl": "https://main.qcloudimg.com/raw/affb3472f8848a5bad492ea4326ff3c3.png",
                "IconUrl": "https://main.qcloudimg.com/raw/a7e4831e6fc893b6e2805e76da851b6b.png",
                "Title": "OOOO",
                "Weight": 112
            }
        ],
        "RequestId": "8dfc397e-f0b0-4b2e-8b6a-3d26c9098c44"
    }
}
```

