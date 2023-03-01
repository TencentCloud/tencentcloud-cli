**Example 1: 出租车发票识别示例代码**

出租车发票识别

Input: 

```
tccli ocr TaxiInvoiceOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "InvoiceNum": "134031321361",
        "InvoiceCode": "15326798",
        "Date": "2018年05月17日",
        "Fare": "19.00",
        "GetOnTime": "16:09",
        "GetOffTime": "16:32",
        "Distance": "9.37",
        "Location": "安徽省蚌埠市",
        "PlateNumber": "C-82851",
        "InvoiceType": "交通",
        "Province": "安徽省",
        "City": "蚌埠市",
        "RequestId": "51766e5b-5382-4480-b517-c893cfaac7f9"
    }
}
```

