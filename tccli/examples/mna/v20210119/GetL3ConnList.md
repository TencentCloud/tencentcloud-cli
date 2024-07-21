**Example 1: 示例1**



Input: 

```
tccli mna GetL3ConnList --cli-unfold-argument  \
    --PageSize 10 \
    --PageNumber 1 \
    --DeviceId abc
```

Output: 
```
{
    "Response": {
        "L3ConnList": [
            {
                "L3ConnId": "abc",
                "DeviceId1": "abc",
                "Cidr1": "xxx",
                "DeviceId2": "cde",
                "Cidr2": "xxx",
                "Enable": true,
                "Description": "abc"
            }
        ],
        "Length": 1,
        "TotalPage": 1,
        "RequestId": "abc"
    }
}
```

