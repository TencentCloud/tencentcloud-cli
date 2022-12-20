**Example 1: 能效标识识别示例**



Input: 

```
tccli ocr RecognizeEnergyLabel --cli-unfold-argument  \
    --ImageBase64 xxx==
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "EnergyLabelList": [
            {
                "Content": "xx",
                "Name": "xx"
            }
        ]
    }
}
```

