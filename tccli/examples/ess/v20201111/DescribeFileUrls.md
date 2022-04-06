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

