**Example 1: 定额发票识别示例代码**

定额发票识别

Input: 

```
tccli ocr QuotaInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg
```

Output: 
```
{
    "Response": {
        "InvoiceNum": "04947858",
        "InvoiceCode": "131001864304",
        "Rate": "伍元",
        "RateNum": "5.00",
        "InvoiceType": "交通",
        "Province": "广东省",
        "City": "深圳市",
        "HasStamp": "1",
        "RequestId": "c0abae2d-10d6-42ae-af0f-a5cc2c9b1fc5"
    }
}
```

