**Example 1: HKIDCardOCR调用**



Input: 

```
tccli ocr HKIDCardOCR --cli-unfold-argument  \
    --ReturnHeadImage False \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg
```

Output: 
```
{
    "Response": {
        "CnName": "申能",
        "EnName": "SAN, Nan",
        "TelexCode": "300000000000",
        "Sex": "女F",
        "Birthday": "01-01-2001",
        "Permanent": 1,
        "IdNum": "C000000(E)",
        "Symbol": "***AZ",
        "FirstIssueDate": "(09-99)",
        "CurrentIssueDate": "23-09-10",
        "HeadImage": null,
        "WarnCardInfos": [
            -9104
        ],
        "RequestId": "fba1c9ad-aeb3-4418-9ecf-80ab1b5fc875",
        "WindowEmbeddedText": "C000000",
        "SmallHeadImage": null
    }
}
```

