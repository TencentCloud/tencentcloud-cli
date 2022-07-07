**Example 1: 智能结构化识别**



Input: 

```
tccli ocr SmartStructuralOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/document/SmartStructuralOCR/SmartStructuralOCR1.jpg \
    --ItemNames 姓名 标题
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "RequestId": "af25f0c0-5c34-4359-98dd-25da408f5947",
        "StructuralItems": [
            {
                "Confidence": 94,
                "ItemCoord": {
                    "Height": 1,
                    "Width": 1,
                    "X": 1,
                    "Y": 0
                },
                "Name": "姓名",
                "Value": "汪晓茹"
            },
            {
                "Confidence": 94,
                "ItemCoord": {
                    "Height": 1,
                    "Width": 1,
                    "X": 1,
                    "Y": 1
                },
                "Name": "标题",
                "Value": "大学英语六级考试成绩报告单"
            }
        ]
    }
}
```

