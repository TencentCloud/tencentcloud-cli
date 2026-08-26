**Example 1: 修改值班表**

修改值班表



Input: 

```
tccli monitor UpdateOnCallForm --cli-unfold-argument  \
    --Module monitor \
    --OnCallFormID form-zahdhgjo \
    --OnCallFormName 值班分组 \
    --OnCallFormDesc 值班分组 \
    --StaffInfos.0.StaffIDs 317528 \
    --RotationType week \
    --ShiftTime 12:00 \
    --EffectiveStartTime 1648742400 \
    --EffectiveEndTime 1649520000 \
    --TimeZone 0 \
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

