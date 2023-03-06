**Example 1: 小票识别**

小票识别

Input: 

```
tccli ocr RecognizeReceiptOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "StoreName": "便民便利店",
        "Number": "00582643",
        "Date": "2022/01/05",
        "Time": "11:11",
        "Total": "1.0",
        "SkuInfos": [
            {
                "ItemName": "中号购物袋",
                "UnitPrice": "0.5",
                "Amount": "1.0"
            }
        ],
        "RequestId": "79b3f0a4-05gd-484a-00fc-302390f546bd"
    }
}
```

