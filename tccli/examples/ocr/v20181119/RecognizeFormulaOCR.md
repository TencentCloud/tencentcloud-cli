**Example 1: 公式识别调用示例**

公式识别调用示例

Input: 

```
tccli ocr RecognizeFormulaOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/edu/RecognizeFormulaOCR/1.png \
    --ImageBase64 /9j/4AAQSk...gABAQ \
    --IsPdf True \
    --PdfPageNumber 1
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "FormulaInfoList": [
            {
                "DetectedText": "求不定积分int",
                "Coord": {
                    "LeftTop": {
                        "X": 0,
                        "Y": 0
                    },
                    "LeftBottom": {
                        "X": 0,
                        "Y": 0
                    },
                    "RightTop": {
                        "X": 0,
                        "Y": 0
                    },
                    "RightBottom": {
                        "X": 0,
                        "Y": 0
                    }
                }
            }
        ],
        "RequestId": "05d49737-c6cf-4678-a9d5-71c008a28e3f"
    }
}
```

