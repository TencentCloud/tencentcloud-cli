**Example 1: 身份证检测告警**

身份证检测

Input: 

```
tccli ocr VerifyGeneralCardWarn --cli-unfold-argument  \
    --CardType 0101 \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/IDCardOCR/IDCardOCR1.jpg
```

Output: 
```
{
    "Response": {
        "Blur": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.01
        },
        "BorderIncomplete": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.01
        },
        "Copy": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.01
        },
        "Cover": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.01
        },
        "Electron": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0
        },
        "Overlap": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.01
        },
        "Reflection": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.01
        },
        "RemakeScreen": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.01
        },
        "Screenshot": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.01
        },
        "Synthesis": {
            "IsWarn": true,
            "Polygon": [],
            "RiskConfidence": 0.9999985
        },
        "Tamper": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0
        },
        "Template": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0
        },
        "TextWatermark": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0
        },
        "WatermarkContent": "",
        "RequestId": "5d75b7af-e03b-45d0-ae0f-1cd00ea06035"
    }
}
```

