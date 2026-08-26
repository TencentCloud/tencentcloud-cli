**Example 1: 查询值班表详情**

查询值班表详情



Input: 

```
tccli monitor DescribeOnCallForm --cli-unfold-argument  \
    --Module monitor \
    --OnCallFormID form-zahdhgjo
```

Output: 
```
{
    "Response": {
        "OnCallForm": {
            "OnCallFormID": "form-zahdhgjo",
            "OnCallFormName": "值班分组",
            "OnCallFormDesc": "值班分组",
            "StaffInfos": [
                {
                    "StaffIDs": [
                        "317528"
                    ]
                }
            ],
            "RotationType": "day",
            "ShiftTime": "12:00",
            "EffectiveStartTime": 1648742400,
            "EffectiveEndTime": 1649520000,
            "TimeZone": 8,
            "CoverStaffInfos": [
                {
                    "CoverStaffIDs": [
                        "317528"
                    ],
                    "CoverStartTime": 1648742400,
                    "CoverEndTime": 1649520000
                }
            ],
            "Tags": [
                {
                    "Key": "petertest",
                    "Value": "petertest"
                }
            ]
        },
        "RequestId": "e3873490-7ca2-4efc-8792-a54e440fe1bd"
    }
}
```

