**Example 1: 查询策略使用上报情况**



Input: 

```
tccli ioa DescribeApplyDevices --cli-unfold-argument  \
    --Update false \
    --AutoUpdate false \
    --PolicyId 474 \
    --OsType 0 \
    --Type 0 \
    --Condition.PageNum 20 \
    --Condition.PageSize 1
```

Output: 
```
{
    "Response": {
        "RequestId": "145c985f-1629-4817-88c7-1740c2d3b951",
        "Data": {
            "Page": {
                "Total": 0,
                "PageCount": 0,
                "PageSize": 1,
                "PageNum": 20
            },
            "DeviceCount": 0,
            "ApplyCount": 0,
            "NotApplyCount": 0,
            "Items": [],
            "UpdateTime": ""
        }
    }
}
```

**Example 2: test**

test

Input: 

```
tccli ioa DescribeApplyDevices --cli-unfold-argument  \
    --Update True \
    --AutoUpdate True \
    --PolicyId 207846 \
    --OsType 0 \
    --Type 0 \
    --Condition.PageSize 1 \
    --Condition.PageNum 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "ApplyCount": 0,
            "DeviceCount": 4,
            "Items": null,
            "NotApplyCount": 4,
            "Page": {
                "PageCount": 4,
                "PageNum": 10,
                "PageSize": 1,
                "Total": 4
            },
            "UpdateTime": "2024-10-15 20:18:34.971"
        },
        "RequestId": "c238f9fb-c1cd-4000-b06e-c990d9628401"
    }
}
```

