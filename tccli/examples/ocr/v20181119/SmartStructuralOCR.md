**Example 1: 智能结构化识别**



Input: 

```
tccli ocr SmartStructuralOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/document/SmartStructuralOCR/SmartStructuralPro1.png \
    --ItemNames 号码
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "StructuralItems": [
            {
                "Name": "号码",
                "Value": "176***101",
                "Confidence": 0,
                "ItemCoord": {
                    "X": 0,
                    "Y": 0,
                    "Width": 0,
                    "Height": 0
                },
                "Row": 0
            }
        ],
        "RequestId": "af25f0c0-5c34-4359-98dd-25da408f5947"
    }
}
```

