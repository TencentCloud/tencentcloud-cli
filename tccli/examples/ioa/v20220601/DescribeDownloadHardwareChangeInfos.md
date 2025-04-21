**Example 1: 示例1**



Input: 

```
tccli ioa DescribeDownloadHardwareChangeInfos --cli-unfold-argument  \
    --EndTime 2022-12-30 \
    --GroupId 392 \
    --BeginTime 2022-10-30
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadURL": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/on-premise/web-open-api/device/TB2rJ8SobM-hardware_change_info-2022-12-30%2017%3A38%3A36.csv?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1672393116%3B1672396716&q-key-time=1672393116%3B1672396716&q-header-list=host&q-url-param-list=&q-signature=01ea2b8f5e186fe559eb3a343605fadb3d8506c0"
        },
        "RequestId": "1c040b34-2514-4211-85a2-7d1f311ee798"
    }
}
```

**Example 2: 测试**

测试

Input: 

```
tccli ioa DescribeDownloadHardwareChangeInfos --cli-unfold-argument  \
    --GroupId 92
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadURL": "https://ioa-dev-1-1258344699.cos.ap-guangzhou.myqcloud.com/on-premise/web-open-api/device/Wka9No9wqh-%E7%BB%88%E7%AB%AF%E7%AE%A1%E7%90%86-%E7%BB%88%E7%AB%AF%E7%A1%AC%E4%BB%B6%E5%8F%98%E6%9B%B4%E4%BF%A1%E6%81%AF-2024-09-09%2010%3A12%3A50.csv?q-sign-algorithm=sha1&q-ak=AKIDOcBdtwlW3LAmETVKxNeiZ1HJ7h5GF1av&q-sign-time=1725847971%3B1725851571&q-key-time=1725847971%3B1725851571&q-header-list=host&q-url-param-list=&q-signature=7f29c8014fefee10e6c53b3a99bde38aea03acc1"
        },
        "RequestId": "21788424-8f47-48c4-a82a-ee7a22204a95"
    }
}
```

