**Example 1: 金融票据切片识别示例代码**

金融票据切片识别示例代码

Input: 

```
tccli ocr FinanBillSliceOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg 
```

Output: 
```
{
    "Response": {
        "FinanBillSliceInfos": [
            {
                "Name": "票号1",
                "Value": "31300051"
            },
            {
                "Name": "票号2",
                "Value": "46686866"
            }
        ],
        "RequestId": "f904eaa3-c868-4a89-9bd9-60afe9635c81"
    }
}
```

