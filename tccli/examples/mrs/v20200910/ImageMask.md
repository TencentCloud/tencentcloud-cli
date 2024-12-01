**Example 1: 医疗报告图片脱敏接口示例**



Input: 

```
tccli mrs ImageMask --cli-unfold-argument  \
    --Image.Base64 注意替换为待脱敏图片的base64编码 \
    --Image.Id 1 \
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
        "MaskedImage": "脱敏后图片的base64编码",
        "RequestId": "1cf14582-bd61-4ea2-93ca-c63eaa8d427a"
    }
}
```

