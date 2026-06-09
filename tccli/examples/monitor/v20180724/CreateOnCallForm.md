**Example 1: 创建值班表**

创建值班表

Input: 

```
tccli monitor CreateOnCallForm --cli-unfold-argument  \
    --Module abc \
    --OnCallFormName abc \
    --OnCallFormDesc abc \
    --StaffInfos.0.StaffIDs abc \
    --RotationType abc \
    --ShiftTime abc \
    --EffectiveStartTime 0 \
    --EffectiveEndTime 0 \
    --TimeZone 0 \
    --CoverStaffInfos.0.CoverStaffIDs abc \
    --CoverStaffInfos.0.CoverStartTime 0 \
    --CoverStaffInfos.0.CoverEndTime 0
```

Output: 
```
{
    "Response": {
        "OnCallFormID": "abc",
        "RequestId": "abc"
    }
}
```

