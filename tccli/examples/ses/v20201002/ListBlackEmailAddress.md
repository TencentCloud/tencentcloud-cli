**Example 1: 获取黑名单邮箱地址**



Input: 

```
tccli ses ListBlackEmailAddress --cli-unfold-argument  \
    --StartDate 2020-09-22 \
    --EndDate 2020-09-22 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "BlackList": [
            {
                "BounceTime": "2023-09-06 11:21:35",
                "EmailAddress": "xxx@gmail.com",
                "IspDesc": "550 5.1.1 The email account that you tried to reach does not exist. Please try\n5.1.1 double-checking the recipient's email addre"
            }
        ],
        "RequestId": "e54b9d01-2bcb-43f6-83dd-55a91a3cd2bb",
        "TotalCount": 2
    }
}
```

