**Example 1: 获取下载文件链接**



Input: 

```
tccli ess DescribeFileUrls --cli-unfold-argument  \
    --Operator.UserId yDxM6UyK********QDV8dJUuO4zjEu \
    --FileType PDF \
    --BusinessType DOCUMENT \
    --FileName 合同 \
    --Limit 0 \
    --Offset 0 \
    --BusinessIds 11114444 11114444555 12315215515 12415251512
```

Output: 
```
{
    "Response": {
        "FileUrls": [
            {
                "Url": "https://file.ess.myqcloud.com/file/xxxx.PDF?key=abc",
                "Option": ""
            },
            {
                "Url": "https://file.ess.myqcloud.com/file/DOCUMENT/xxxx.PDF?key=abc",
                "Option": ""
            },
            {
                "Url": "https://file.ess.myqcloud.com/file/DOCUMENT/xxx.PDF?key=abc",
                "Option": ""
            },
            {
                "Url": "https://file.ess.myqcloud.com/file/DOCUMENT/xxx.PDF?key=abc",
                "Option": ""
            }
        ],
        "TotalCount": 4,
        "RequestId": "XXXX"
    }
}
```

**Example 2: 获取下载文件链接 --- 压缩多文件**



Input: 

```
tccli ess DescribeFileUrls --cli-unfold-argument  \
    --Operator.UserId f2d8********f56b7 \
    --FileType ZIP \
    --BusinessType DOCUMENT \
    --FileName 合同 \
    --Limit 0 \
    --Offset 0 \
    --BusinessIds e1a5****dfabfdbec6 670d****590d4dcd dc3df****07f8323
```

Output: 
```
{
    "Response": {
        "FileUrls": [
            {
                "Url": "https://file.ess.myqcloud.com/files/DOCUMENT/xxxx.ZIP?key=key********1234",
                "Option": ""
            }
        ],
        "TotalCount": 1,
        "RequestId": "XXXX"
    }
}
```

**Example 3: a**



Input: 

```
tccli ess DescribeFileUrls --cli-unfold-argument  \
    --Operator.UserId yDRtRUUgygqa2mtyUuO4zjEyckqC592v \
    --BusinessType FLOW \
    --BusinessIds yDR0dUUgygqih0oeUuO4zjEvWe1SbE7r
```

Output: 
```
{
    "Response": {
        "FileUrls": [
            {
                "Option": "[\"595.00,841.00\",\"-1\"]",
                "Url": "https://file.test.ess.tencent.cn/file/FLOW/yDR0dUUgygqih0oeUuO4zjEvWe1SbE7r/0/0.PDF?hkey=c80b3f135787e86cbd1841a17211ca7f86c7cf8e40059df26bb6b554ffa8b93d603ac6e1ff343bd1addcf442cc41c5f7a4588fe828bb561819896ab91e04f0780907adeb70e3005cc2e466afd14599c6f04521e619fb6fa0ad002ad82345c777"
            }
        ],
        "RequestId": "1e1da501-8c68-4ce4-a982-5d570ab151c9",
        "TotalCount": 1
    }
}
```

