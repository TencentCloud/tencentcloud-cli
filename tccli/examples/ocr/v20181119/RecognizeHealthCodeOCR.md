**Example 1: 健康码识别示例代码**

健康码识别

Input: 

```
tccli ocr RecognizeHealthCodeOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Color": "绿色",
        "IDNumber": "",
        "Name": "王*一",
        "RequestId": "632c1770-ef32-45e3-b4fc-2cc93ac0bad3",
        "SpotName": "",
        "TestingInterval": "48小时",
        "TestingResult": "阴性",
        "TestingTime": "2022-01-15 22:52",
        "Time": "01-08 17:05:05",
        "Vaccination": "已完成全程接种",
        "VaccinationTime": "2021-07-25"
    }
}
```

