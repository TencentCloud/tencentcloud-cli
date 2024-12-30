**Example 1: 获取ocr的token值**

获取身份证ocr的token值，开启所有告警

Input: 

```
tccli ocr GetOCRToken --cli-unfold-argument  \
    --Type IDCardOCR \
    --IDCardConfig.CopyWarn True \
    --IDCardConfig.BorderCheckWarn True \
    --IDCardConfig.ReshootWarn True \
    --IDCardConfig.DetectPsWarn True \
    --IDCardConfig.TempIdWarn True \
    --IDCardConfig.InvalidDateWarn True \
    --IDCardConfig.ReflectWarn True
```

Output: 
```
{
    "Response": {
        "OCRToken": "09FEF899-3B43-46C6-87F6-FFD3D7EC9B59",
        "RequestId": "d1d679c5-85fc-414a-a32b-8e5225023a6e"
    }
}
```

