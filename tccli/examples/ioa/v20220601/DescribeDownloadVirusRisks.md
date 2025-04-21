**Example 1: 示例1**



Input: 

```
tccli ioa DescribeDownloadVirusRisks --cli-unfold-argument  \
    --Mid F1AFD85EC54480393C546B99C7CD014963761895
```

Output: 
```
{
    "Response": {
        "RequestId": "f2d9cd92-3f4d-47cf-807d-1f1f5f307d04",
        "Data": {
            "DownloadURL": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/on-premise/security-open-api/virus/lLigzjOqCo-%E7%BB%88%E7%AB%AF%E7%AE%A1%E7%90%86-%E7%97%85%E6%AF%92%E6%9F%A5%E6%9D%80-%E6%9C%AA%E5%A4%84%E7%90%86%E9%A3%8E%E9%99%A9%E5%88%97%E8%A1%A8-20221222192132.csv?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1671708092%3B1671711692&q-key-time=1671708092%3B1671711692&q-header-list=host&q-url-param-list=&q-signature=77ffdb53c1877599784e72457ba6f3f43008d268"
        }
    }
}
```

**Example 2: DescribeDownloadVirusRisks**

DescribeDownloadVirusRisks

Input: 

```
tccli ioa DescribeDownloadVirusRisks --cli-unfold-argument  \
    --Mid 123456
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "f33aa9d9-a2c2-45d3-9f84-1b658c9a0eb8"
    }
}
```

