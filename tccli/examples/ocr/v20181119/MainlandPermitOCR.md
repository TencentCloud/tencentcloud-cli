**Example 1: 港澳台来往内地通行证识别示例代码**

港澳台来往内地通行证识别

Input: 

```
tccli ocr MainlandPermitOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --RetProfile False
```

Output: 
```
{
    "Response": {
        "Name": "李明",
        "EnglishName": "LIMING",
        "Number": "C00000000",
        "Sex": "男",
        "ValidDate": "2018.10.09-2028.10.08",
        "IssueAuthority": "公安部出入境管理局",
        "IssueAddress": "广东",
        "Birthday": "1981.08.03",
        "IssueNumber": "02",
        "Type": "台湾居民来往大陆通行证",
        "Profile": "",
        "RequestId": "3090debe-3662-4ef1-8784-6ef2fb59f75e"
    }
}
```

