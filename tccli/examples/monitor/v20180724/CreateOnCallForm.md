**Example 1: 创建值班表**

创建值班表

Input: 

```
tccli monitor CreateOnCallForm --cli-unfold-argument  \
    --Module monitor \
    --OnCallFormName 值班分组 \
    --OnCallFormDesc 值班分组 \
    --StaffInfos.0.StaffIDs 317528 \
    --RotationType day \
    --ShiftTime 12:00 \
    --EffectiveStartTime 1648742400 \
    --EffectiveEndTime 1649520000 \
    --TimeZone 8 \
    --CoverStaffInfos.0.CoverStaffIDs 317528 \
    --CoverStaffInfos.0.CoverStartTime 1648742400 \
    --CoverStaffInfos.0.CoverEndTime 1649520000
```

Output: 
```
{
    "Response": {
        "OnCallFormID": "form-zahdhgjo",
        "RequestId": "e3873490-7ca2-4efc-8792-a54e440fe1bd"
    }
}
```

