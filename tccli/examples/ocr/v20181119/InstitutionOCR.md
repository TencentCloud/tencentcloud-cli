**Example 1: 事业单位法人证书识别示例代码**

事业单位法人证书关键字段识别，包括注册号、有效期、住所、名称、法定代表人等

Input: 

```
tccli ocr InstitutionOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg 
```

Output: 
```
{
    "Response": {
        "LegalPerson": "李明",
        "Location": "武汉市武昌区雄楚路123号",
        "Name": "长江交通职业技术学院",
        "RegId": "",
        "RequestId": "3824099f-bf5b-40a2-af13-11dfca689f55",
        "ValidDate": "自2015年03月30日至2020年03月30日"
    }
}
```

