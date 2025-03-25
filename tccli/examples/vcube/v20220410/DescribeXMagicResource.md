**Example 1: 获取优图资源包**

获取优图资源包

Input: 

```
tccli vcube DescribeXMagicResource --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Count": 2,
        "RequestId": "37613734-ebdd-4473-afb4-b341f57388e4",
        "Resources": [
            {
                "AppId": "1328524534",
                "BizType": "xmagic",
                "CreatedAt": "2024-12-18T06:01:14.259Z",
                "Duration": "1",
                "EndTime": "2025-12-18T14:01:14+08:00",
                "Expired": false,
                "Id": 110,
                "IsUse": true,
                "Name": "Advanced S100",
                "Plan": "S1-00",
                "ResourceId": "xmc34868456f193d85b2d13",
                "StartTime": "2024-12-18T14:01:14+08:00",
                "UpdatedAt": "2024-12-18T06:01:14.259Z",
                "XMagic": false,
                "XMagicType": "combined"
            },
            {
                "AppId": "1328524534",
                "BizType": "xmagic",
                "CreatedAt": "2024-11-18T09:29:21.291Z",
                "Duration": "1",
                "EndTime": "2024-12-18T17:29:21+08:00",
                "Expired": false,
                "Id": 107,
                "IsUse": true,
                "Name": "Basic A102",
                "Plan": "A1-02",
                "ResourceId": "xmc42ace356133e9aee85",
                "StartTime": "2024-11-18T17:29:21+08:00",
                "UpdatedAt": "2024-11-18T09:29:21.291Z",
                "XMagic": false,
                "XMagicType": "combined"
            }
        ]
    }
}
```

