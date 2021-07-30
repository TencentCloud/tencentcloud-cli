**Example 1: 获取设备云存服务详情**



Input: 

```
tccli iotvideo DescribeCloudStorage --cli-unfold-argument  \
    --ProductId H541SOP191 \
    --DeviceName event_36502632_1 \
    --UserId default
```

Output: 
```
{
    "Response": {
        "RequestId": "f889deee-70ec-4391-9b91-bb0f3f09b5a4",
        "Status": 1,
        "Type": 1,
        "ExpireTime": 1614670782,
        "ShiftDuration": 86400,
        "UserId": "default"
    }
}
```

