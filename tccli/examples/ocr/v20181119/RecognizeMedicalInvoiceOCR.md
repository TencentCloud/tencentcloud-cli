**Example 1: 医疗发票识别示例**

医疗发票识别示例

Input: 

```
tccli ocr RecognizeMedicalInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/invoice/RecognizeMedicalInvoiceOCR/RecognizeMedicalInvoiceOCR1.jpg \
    --ReturnVertex True \
    --ReturnCoord True
```

Output: 
```
{
    "Response": {
        "MedicalInvoiceInfos": [
            {
                "MedicalInvoiceItems": [
                    {
                        "Name": "单位",
                        "Content": "***机构",
                        "Vertex": {
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
                        },
                        "Coord": {
                            "X": 0,
                            "Y": 0,
                            "Width": 0,
                            "Height": 0
                        }
                    }
                ]
            }
        ],
        "Angle": 0,
        "RequestId": "cb2ba647-06bd-447d-95c6-7d6264eaa8b0"
    }
}
```

