**Example 1: 医疗报告图片脱敏异步接口示例**



Input: 

```
tccli mrs ImageMaskAsync --cli-unfold-argument  \
    --Image.Id 1 \
    --Image.Url abc \
    --Image.Base64 abc \
    --MaskFlag.HospitalFlag True \
    --MaskFlag.DoctorFlag True \
    --MaskFlag.PatientFlag True \
    --MaskFlag.BarFlag True \
    --AutoFixImageDirection True
```

Output: 
```
{
    "Response": {
        "TaskID": "abc",
        "RequestId": "abc"
    }
}
```

