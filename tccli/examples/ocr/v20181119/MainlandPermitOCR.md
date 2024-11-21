**Example 1: MainlandPermitOCR调用**

MainlandPermitOCR调用

Input: 

```
tccli ocr MainlandPermitOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/MainlandPermitOCR/MainlandPermitOCR1.png \
    --RetProfile False
```

Output: 
```
{
    "Response": {
        "Birthday": "1986.03.02",
        "EnglishName": "LI,YOU-TU",
        "IssueAddress": "广东",
        "IssueAuthority": "公安部出入境管理局",
        "IssueNumber": "02",
        "MainlandTravelPermitBackInfos": {
            "HistoryNumber": "",
            "IDNumber": "",
            "Name": "",
            "Type": "台湾居民来往大陆通行证"
        },
        "Name": "李优图",
        "Nationality": "",
        "Number": "08320271",
        "Profile": "",
        "RequestId": "bd8fb0bc-6558-48b5-b057-2b04edacf225",
        "Sex": "男",
        "Type": "台湾居民来往大陆通行证",
        "ValidDate": "2016.02.03-2021.02.02"
    }
}
```

