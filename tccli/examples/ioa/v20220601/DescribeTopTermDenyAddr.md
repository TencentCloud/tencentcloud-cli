**Example 1: 示例1**

示例1

Input: 

```
tccli ioa DescribeTopTermDenyAddr --cli-unfold-argument  \
    --StartTime 1683703604000 \
    --EndTime 1685431604000 \
    --From 0 \
    --Size 10 \
    --Sort desc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": [
                {
                    "Count": 2,
                    "Rank": 1,
                    "Url": "www.taobao.com",
                    "WebSiteTypeName": ""
                },
                {
                    "Count": 1,
                    "Rank": 2,
                    "Url": "www.x1kkx11a.com",
                    "WebSiteTypeName": "内置网址"
                },
                {
                    "Count": 1,
                    "Rank": 3,
                    "Url": "www.x1kkx12s11a.com",
                    "WebSiteTypeName": "自定义网址"
                },
                {
                    "Count": 1,
                    "Rank": 4,
                    "Url": "www.xkk.com",
                    "WebSiteTypeName": "内置网址"
                },
                {
                    "Count": 1,
                    "Rank": 5,
                    "Url": "www.xkkx11a.com",
                    "WebSiteTypeName": "内置网址"
                },
                {
                    "Count": 1,
                    "Rank": 6,
                    "Url": "www.xkkxa.com",
                    "WebSiteTypeName": "内置网址"
                },
                {
                    "Count": 1,
                    "Rank": 7,
                    "Url": "www.xxx.com",
                    "WebSiteTypeName": ""
                },
                {
                    "Count": 1,
                    "Rank": 8,
                    "Url": "www.xzc.com",
                    "WebSiteTypeName": "-"
                },
                {
                    "Count": 1,
                    "Rank": 9,
                    "Url": "www.yyy.com",
                    "WebSiteTypeName": ""
                },
                {
                    "Count": 1,
                    "Rank": 10,
                    "Url": "www.zzz.com",
                    "WebSiteTypeName": "-"
                }
            ],
            "Total": 10
        },
        "RequestId": "c4d2e703-6207-47bc-87dc-ab38d185c21e"
    }
}
```

**Example 2: DescribeTopTermDenyAddr**

DescribeTopTermDenyAddr

Input: 

```
tccli ioa DescribeTopTermDenyAddr --cli-unfold-argument  \
    --StartTime 1 \
    --EndTime 1 \
    --Department 1 \
    --From 1 \
    --Size 1 \
    --Sort 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "8147d2b6-d645-49bb-81c8-c2247d434a4b"
    }
}
```

