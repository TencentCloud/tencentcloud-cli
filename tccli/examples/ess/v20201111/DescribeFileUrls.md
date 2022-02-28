**Example 1: 获取下载文件链接**



Input: 

```
tccli ess DescribeFileUrls --cli-unfold-argument  \
    --Operator.Channel string \
    --Operator.ClientIp 1.1.1.1 \
    --Operator.OpenId 321654 \
    --Operator.ProxyIp 2.2.2.2 \
    --Operator.UserId 11234567890123456789012345678901 \
    --FileType PDF \
    --BusinessType DOCUMENT \
    --FileName 西安合同 \
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
                "Url": "https://file.ess.myqcloud.com/file/DOCUMENT/11114444555/0/0.PDF?key=1a153dbfb56f46c8653b901a60009589",
                "Option": ""
            },
            {
                "Url": "https://file.ess.myqcloud.com/file/DOCUMENT/12315215515/0/0.PDF?key=1a153dbfb56f46c8653b901a60009589",
                "Option": ""
            },
            {
                "Url": "https://file.ess.myqcloud.com/file/DOCUMENT/12415251512/0/0.PDF?key=1a153dbfb56f46c8653b901a60009589",
                "Option": ""
            },
            {
                "Url": "https://file.ess.myqcloud.com/file/DOCUMENT/11114444/0/0.PDF?key=1a153dbfb56f46c8653b901a60009589",
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
    --Operator.Channel string \
    --Operator.ClientIp 1.1.1.1 \
    --Operator.OpenId 321654 \
    --Operator.ProxyIp 2.2.2.2 \
    --Operator.UserId 11234567890123456789012345678901 \
    --FileType ZIP \
    --BusinessType DOCUMENT \
    --FileName 西安合同 \
    --Limit 0 \
    --Offset 0 \
    --BusinessIds 11114444555 12315215515 12415251512
```

Output: 
```
{
    "Response": {
        "FileUrls": [
            {
                "Url": "https://file.ess.myqcloud.com/files/DOCUMENT/11114444555,12315215515,12415251512/0/0.ZIP?key=1a153dbfb56f46c8653b901a60009589",
                "Option": ""
            }
        ],
        "TotalCount": 1,
        "RequestId": "XXXX"
    }
}
```

