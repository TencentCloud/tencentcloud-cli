**Example 1: 医疗报告图片脱敏异步接口示例**



Input: 

```
tccli mrs ImageMaskAsync --cli-unfold-argument  \
    --Image.Base64 注意替换为待脱敏图片base64编码 \
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
        "TaskID": "任务ID,之后使用这个任务ID调用 ImageMaskAsyncGetResult 接口获取脱敏后的图片",
        "RequestId": "0a133433-d199-4728-b58e-18aeda282fb0"
    }
}
```

