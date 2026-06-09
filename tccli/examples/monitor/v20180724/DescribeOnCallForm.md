**Example 1: 查询值班表详情**

查询值班表详情



Input: 

```
tccli monitor DescribeOnCallForm --cli-unfold-argument  \
    --Module abc \
    --OnCallFormID abc
```

Output: 
```
{
    "Response": {
        "OnCallForm": {
            "OnCallFormID": "abc",
            "OnCallFormName": "abc",
            "OnCallFormDesc": "abc",
            "StaffInfos": [
                {
                    "StaffIDs": [
                        "abc"
                    ]
                }
            ],
            "RotationType": "abc",
            "ShiftTime": "abc",
            "EffectiveStartTime": 0,
            "EffectiveEndTime": 0,
            "TimeZone": 0,
            "CoverStaffInfos": [
                {
                    "CoverStaffIDs": [
                        "abc"
                    ],
                    "CoverStartTime": 0,
                    "CoverEndTime": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

