**Example 1: 中国香港身份证识别示例代码**



Input: 

```
tccli ocr HKIDCardOCR --cli-unfold-argument  \
    --DetectFake true \
    --ReturnHeadImage false \
    --ImageUrl https://xx/a.jpg
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
        "FakeDetectResult": 1,
        "WarningCode": [
            -9102,
            -9103
        ],
        "HeadImage": "",
        "RequestId": "fba1c9ad-aeb3-4418-9ecf-80ab1b5fc875"
    }
}
```

