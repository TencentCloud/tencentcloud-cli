**Example 1: 运单识别示例代码**

运单识别示例代码

Input: 

```
tccli ocr WaybillOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "TextDetections": {
            "RecName": {
                "Text": "李明"
            },
            "RecAddr": {
                "Text": "上海市,上海市，徐汇区,古美路1528号A1幢2楼"
            },
            "RecNum": {
                "Text": "18812152888"
            },
            "SenderName": {
                "Text": "海购商品"
            },
            "SenderNum": {
                "Text": "021-54569595"
            },
            "SenderAddr": {
                "Text": "杭州市江干区12号路口跨境贸易电子商务产业园"
            },
            "WaybillNum": {
                "Text": "456732006925"
            }
        },
        "RequestId": "0c447696-cb8d-4686-8336-7c146e3f62cc"
    }
}
```

