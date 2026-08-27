**Example 1: 查询值班列表**

查询值班列表

Input: 

```
tccli monitor DescribeOnCallForms --cli-unfold-argument  \
    --Module monitor \
    --OnCallFormStaffIDs 317528 \
    --RotationType day \
    --Offset 1 \
    --Limit 10 \
    --Order desc \
    --OnCallFormName 值班分组
```

Output: 
```
{
    "Response": {
        "OnCallForms": [
            {
                "OnCallFormID": "form-zahdhgjo",
                "OnCallFormName": "值班分组",
                "OnCallFormDesc": "值班分组",
                "RotationType": "day",
                "ShiftTime": "12:00",
                "EffectiveStartTime": 1648742400,
                "EffectiveEndTime": 1649520000,
                "TimeZone": 8,
                "CurrOnCallStaffs": [
                    "317528"
                ],
                "Tags": [
                    {
                        "Key": "petertest",
                        "Value": "petertest"
                    }
                ]
            }
        ],
        "TotalCount": 10,
        "RequestId": "e3873490-7ca2-4efc-8792-77"
    }
}
```

