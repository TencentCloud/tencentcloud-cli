**Example 1: 组织机构代码证识别示例代码**

组织机构代码证识别

Input: 

```
tccli ocr OrgCodeCertOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg 
```

Output: 
```
{
    "Response": {
        "OrgCode": "300000-3",
        "Name": "望江县xxx店",
        "Address": "望江县天鹅购物广场xxx铺",
        "ValidDate": "自2019年07月01日至2023年06月30日",
        "RequestId": "e7fdecd4-39a3-46a7-a565-274a2004af2e"
    }
}
```

