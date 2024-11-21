**Example 1: 医疗报告图片脱敏接口示例**



Input: 

```
tccli mrs ImageMask --cli-unfold-argument  \
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
        "MaskedImage": "abc",
        "RequestId": "abc"
    }
}
```

