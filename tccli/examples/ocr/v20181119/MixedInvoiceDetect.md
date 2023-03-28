**Example 1: 混贴票据分类示例代码**

混贴票据分类

Input: 

```
tccli ocr MixedInvoiceDetect --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --ReturnImage False
```

Output: 
```
{
    "Response": {
        "InvoiceDetectInfos": [
            {
                "Angle": 0,
                "Type": 3,
                "Rect": {
                    "X": 19,
                    "Y": 43,
                    "Width": 1340,
                    "Height": 852
                },
                "Image": null
            },
            {
                "Angle": 0,
                "Type": 13,
                "Rect": {
                    "X": 20,
                    "Y": 891,
                    "Width": 479,
                    "Height": 597
                },
                "Image": null
            },
            {
                "Angle": 0,
                "Type": 2,
                "Rect": {
                    "X": 520,
                    "Y": 904,
                    "Width": 455,
                    "Height": 286
                },
                "Image": null
            }
        ],
        "RequestId": "c8cedc79-d03b-463d-8b95-b807b4ca5135"
    }
}
```

