**Example 1: 基于软件查看终端详情列表**



Input: 

```
tccli ioa DescribeDeviceDetailList --cli-unfold-argument  \
    --OsType 0 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "cfe7fa02-dfd7-4ff2-9b3f-4f645ad03ced",
        "Data": {
            "Page": {
                "Total": 0,
                "PageCount": 0,
                "PageSize": 1000,
                "PageNum": 1
            },
            "Items": []
        }
    }
}
```

