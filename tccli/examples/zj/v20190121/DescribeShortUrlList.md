**Example 1: DescribeShortUrlList**



Input: 

```
tccli zj DescribeShortUrlList --cli-unfold-argument  \
    --License KA3431QZPU \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Count": 1,
            "List": [
                {
                    "ShortUrlId": "281",
                    "FullUrl": "https://www.qq.com/uu",
                    "ShortUrl": "https://url.cn/7P2df2II",
                    "Name": "测试",
                    "EndDate": "2021-07-04 14:39:26",
                    "CreatedAt": "2021-06-04 14:39:26",
                    "UrlType": 0,
                    "Status": 0,
                    "Style": 0,
                    "MiniProgramId": "",
                    "MiniProgramName": "",
                    "MiddlePageId": 0
                }
            ]
        },
        "RequestId": "111111"
    }
}
```

