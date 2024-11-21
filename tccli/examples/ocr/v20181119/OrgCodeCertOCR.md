**Example 1: OrgCodeCertOCR调用**



Input: 

```
tccli ocr OrgCodeCertOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg
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

