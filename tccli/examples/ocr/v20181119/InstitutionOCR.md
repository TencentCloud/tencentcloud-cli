**Example 1: InstitutionOCR调用**



Input: 

```
tccli ocr InstitutionOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg
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

