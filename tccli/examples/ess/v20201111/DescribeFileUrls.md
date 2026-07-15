**Example 1: 查询的文件没有权限**



Input: 

```
tccli ess DescribeFileUrls --cli-unfold-argument  \
    --Operator.UserId yDxM6UyK********QDV8dJUuO4zjEu \
    --FileType PDF \
    --BusinessType FLOW \
    --FileName 合同 \
    --Limit 0 \
    --Offset 0 \
    --BusinessIds 11114444 11114444555 12315215515 12415251512
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound",
            "Message": "资源不存在或无权限"
        },
        "RequestId": "s166*******3046"
    }
}
```

**Example 2: 获取下载文件链接 --- 单个合同**

下载单个合同文件

Input: 

```
tccli ess DescribeFileUrls --cli-unfold-argument  \
    --Operator.UserId yDRSRUUgygj6qnwfUuO4zjEwc193c2hH \
    --BusinessType FLOW \
    --BusinessIds yDwFkUUckpstzjhfUugNAWf1KibXqS26
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

**Example 3: 获取下载文件链接 --- 压缩多文件**

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

**Example 4: 获取下载文件链接 --- 多个文件**

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

**Example 5: 获取合同的图片链接**



Input: 

```
tccli ess DescribeFileUrls --cli-unfold-argument  \
    --Operator.UserId yDw6yUUgyg3caowzUx4GQptRKfMnJqX8 \
    --BusinessType FLOW \
    --BusinessIds yDtGEUUckp95ebqbUxQS8nN8JR1lqIvb \
    --FileType JPG
```

Output: 
```
{
    "Response": {
        "FileUrls": [
            {
                "Option": "{\"width\":595.32,\"height\":841.92}",
                "Url": "https://file.test.ess.tencent.cn/file/FLOW/yDtGEUUckp95ebqbUxQS8nN8JR1lqIvb/0/0.JPG?hkey=e01db63a678fcda3d"
            },
            {
                "Option": "{\"width\":595.32,\"height\":841.92}",
                "Url": "https://file.test.ess.tencent.cn/file/FLOW/yDtGEUUckp95ebqbUxQS8nN8JR1lqIvb/0/1.JPG?hkey=e01db63a678fcda3dba85"
            },
            {
                "Option": "{\"width\":595.32,\"height\":841.92}",
                "Url": "https://file.test.ess.tencent.cn/file/FLOW/yDtGEUUckp95ebqbUxQS8nN8JR1lqIvb/0/2.JPG?hkey=e01db63a678fcda3dba85d1b"
            },
            {
                "Option": "{\"width\":595.28,\"height\":841.89}",
                "Url": "https://file.test.ess.tencent.cn/file/FLOW/yDtGEUUckp95ebqbUxQS8nN8JR1lqIvb/0/3.JPG?hkey=e01db63a678044f08e14f9870532559c"
            },
            {
                "Option": "{\"width\":595.28,\"height\":841.89}",
                "Url": "https://file.test.ess.tencent.cn/file/FLOW/yDtGEUUckp95ebqbUxQS8nN8JR1lqIvb/0/4.JPG?hkey=e01db63a678fcda3d2559c"
            },
            {
                "Option": "{\"width\":595.28,\"height\":841.89}",
                "Url": "https://file.test.ess.tencent.cn/file/FLOW/yDtGEUUckp95ebqbUxQS8nN8JR1lqIvb/0/5.JPG?hkey=e01db63a678fcda3dba85d"
            }
        ],
        "RequestId": "4e02b62e-162b-4f57-8567-0cf257da2c72",
        "TotalCount": 6
    }
}
```

