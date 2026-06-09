**Example 1: 查询值班列表**

查询值班列表

Input: 

```
tccli monitor DescribeOnCallForms --cli-unfold-argument  \
    --Module abc \
    --OnCallFormStaffIDs abc \
    --RotationType abc \
    --Offset 0 \
    --Limit 0 \
    --Order abc \
    --OnCallFormName abc
```

Output: 
```
{
    "Response": {
        "OnCallForms": [
            {
                "OnCallFormID": "abc",
                "OnCallFormName": "abc",
                "OnCallFormDesc": "abc",
                "RotationType": "abc",
                "ShiftTime": "abc",
                "EffectiveStartTime": 0,
                "EffectiveEndTime": 0,
                "TimeZone": 0,
                "CurrOnCallStaffs": [
                    "abc"
                ]
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

