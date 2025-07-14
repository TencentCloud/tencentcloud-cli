**Example 1: 示例1**



Input: 

```
tccli ioa DescribeDownloadViruses --cli-unfold-argument  \
    --OsType 0 \
    --OnlineStatus 1 \
    --RiskStatus 1 \
    --GroupId 392
```

Output: 
```
{
    "Response": {
        "RequestId": "35d14ba7-e754-453e-9db8-96c10c21ec74",
        "Data": {
            "DownloadURL": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/on-premise/security-open-api/virus/TB2rJ8SobM-%E7%97%85%E6%AF%92%E6%9F%A5%E6%9D%80-%E9%A3%8E%E9%99%A9%E5%88%97%E8%A1%A8-20221222191456.csv?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1671707696%3B1671711296&q-key-time=1671707696%3B1671711296&q-header-list=host&q-url-param-list=&q-signature=46046a4ed18f649cc95b82b6fa232e80f9493563"
        }
    }
}
```

**Example 2: DescribeDownloadViruses**

DescribeDownloadViruses

Input: 

```
tccli ioa DescribeDownloadViruses --cli-unfold-argument  \
    --DomainInstanceId 13 \
    --OsType 13 \
    --OnlineStatus 1 \
    --GroupId 1 \
    --Condition.PageSize 1 \
    --Condition.PageNum 1 \
    --RiskStatus 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "46fca9b9-2df3-4655-8dcd-9ed1f2bbb27e"
    }
}
```

