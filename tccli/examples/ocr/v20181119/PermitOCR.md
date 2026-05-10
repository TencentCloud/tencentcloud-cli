**Example 1: PermitOCR调用**



Input: 

```
tccli ocr PermitOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/PermitOCR/PermitOCR1.jpg
```

Output: 
```
{
    "Response": {
        "Birthday": "1900.10.27",
        "EnglishName": "XXX,XXXX",
        "IssueAddress": "XX",
        "IssueAuthority": "公安部出入境管理局",
        "Name": "某某某",
        "Number": "C900001111",
        "PortraitImage": "",
        "RequestId": "fedf285d-60bc-4e46-8d27-3f1d80bb19f6",
        "Sex": "女",
        "Type": "往来港澳通行证",
        "ValidDate": "2018.10.09-2028.10.08"
    }
}
```

