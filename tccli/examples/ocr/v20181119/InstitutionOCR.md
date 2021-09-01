**Example 1: 事业单位法人证书识别示例代码**



Input: 

```
tccli ocr InstitutionOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "RegId": "100XXX",
        "ValidDate": "自xxxx年xx月xx日至20xx年xx月xx日",
        "Location": "武汉市武昌区雄楚路xxx号",
        "Name": "长江",
        "LegalPerson": "xx",
        "RequestId": "d60bba4c-9000-4387-8834-bef92e80142f"
    }
}
```

