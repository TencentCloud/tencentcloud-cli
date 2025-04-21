**Example 1: 示例1**



Input: 

```
tccli ioa DescribeDeviceCompliantInfos --cli-unfold-argument  \
    --OsType 0 \
    --OnlineStatus 1 \
    --ResultStatus 1 \
    --GroupId 392
```

Output: 
```
{
    "Response": {
        "RequestId": "04d4510e-d73b-4192-a375-3179bf126cf5",
        "Data": {
            "Paging": {
                "PageSize": 10,
                "PageNum": 1,
                "PageCount": 0,
                "Total": 0
            },
            "Items": []
        }
    }
}
```

**Example 2: DescribeDeviceCompliantInfo**

DescribeDeviceCompliantInfo

Input: 

```
tccli ioa DescribeDeviceCompliantInfos --cli-unfold-argument  \
    --GroupId 1 \
    --OsType 0 \
    --OnlineStatus 1 \
    --ResultStatus 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "5fb53dd5-0b63-4bfe-af36-ccdefb53a46a"
    }
}
```

