**Example 1: 获取下载文件链接 --- 压缩多文件**

下载文件压缩包

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

**Example 2: 获取下载文件链接 --- 单个文件**

下载单个合同文件

Input: 

```
tccli ess DescribeFileUrls --cli-unfold-argument  \
    --Operator.UserId yDRtRUUgxxxxxx4zjEyckqC592v \
    --BusinessType FLOW \
    --BusinessIds yDR0dUUgxxxxxxjEvWe1SbE7r
```

Output: 
```
{
    "Response": {
        "FileUrls": [
            {
                "Option": "[\"595.00,841.00\",\"-1\"]",
                "Url": "https://file.test.ess.tencent.cn/file/FLOW/yDR0dUxxxxxxxxWe1SbE7r/0/0.PDF?hkey=c80b3f1357821exxxxxxxxxxx2ad82345c777"
            }
        ],
        "RequestId": "1e1da50xxxxxx5d570ab151c9",
        "TotalCount": 1
    }
}
```

**Example 3: 获取下载文件链接 --- 多个文件**

下载多个合同文件

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

