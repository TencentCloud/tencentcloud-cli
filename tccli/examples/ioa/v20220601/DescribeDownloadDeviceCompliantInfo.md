**Example 1: 示例1**



Input: 

```
tccli ioa DescribeDownloadDeviceCompliantInfo --cli-unfold-argument  \
    --OsType 0 \
    --OnlineStatus 1 \
    --ResultStatus 1 \
    --GroupId 392
```

Output: 
```
{
    "Response": {
        "RequestId": "1d6d20f7-fd66-4a42-86b9-9efcc1098705",
        "Data": {
            "DownloadURL": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/on-premise/security-open-api/compliant/bmLXIwYohX-%E4%BA%8B%E4%BB%B6%E4%B8%AD%E5%BF%83-%E8%AE%BE%E5%A4%87%E5%90%88%E8%A7%84%E6%A3%80%E6%9F%A5-20221222193016.csv?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1671708617%3B1671712217&q-key-time=1671708617%3B1671712217&q-header-list=host&q-url-param-list=&q-signature=001ef50e5c5a1c87b3c0b5604c7808971d539f69"
        }
    }
}
```

**Example 2: DescribeDownloadDeviceCompliantInfo**

DescribeDownloadDeviceCompliantInfo

Input: 

```
tccli ioa DescribeDownloadDeviceCompliantInfo --cli-unfold-argument  \
    --GroupId 1 \
    --OsType 1 \
    --OnlineStatus 1 \
    --ResultStatus 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "a73d2631-e50f-438d-8577-4ffb20fef170"
    }
}
```

