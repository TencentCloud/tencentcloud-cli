**Example 1: 户口本识别示例代码**



Input: 

```
tccli ocr ResidenceBookletOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "HouseholdNumber": "000006498",
        "Name": "喻玺",
        "Sex": "男",
        "BirthPlace": "四川省合江县",
        "Nation": "汉族",
        "NativePlace": "四川省合江县",
        "BirthDate": "1980年1月11日",
        "IdCardNumber": "510522198001110255",
        "EducationDegree": "高中毕业",
        "ServicePlace": "合江镇",
        "Household": "家庭户",
        "Address": "上海市徐汇区田林路397号腾云大厦",
        "RequestId": "973edeb4-d0a1-4e6c-aa9c-fdfc7b24b357"
    }
}
```

