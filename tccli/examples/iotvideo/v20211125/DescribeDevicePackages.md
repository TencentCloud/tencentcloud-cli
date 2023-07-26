**Example 1: 拉取有效套餐列表**



Input: 

```
tccli iotvideo DescribeDevicePackages --cli-unfold-argument  \
    --ProductId abc \
    --DeviceName abc \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Packages": [
            {
                "Status": 0,
                "CSType": 1,
                "CSShiftDuration": 1,
                "CSExpiredTime": 0,
                "CreatedAt": 0,
                "UpdatedAt": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

