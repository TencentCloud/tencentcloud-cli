**Example 1: 能效标识识别示例**

能效标识识别示例

Input: 

```
tccli ocr RecognizeEnergyLabel --cli-unfold-argument  \
    --ImageBase64 xxx==
```

Output: 
```
{
    "Response": {
        "EnergyLabelList": [
            {
                "Content": " 1级",
                "Name": "能效等级"
            },
            {
                "Content": "空调",
                "Name": "家电类型"
            }
        ],
        "RequestId": "16f35cd8-e846-4bdf-acad-73b34e11789c"
    }
}
```

