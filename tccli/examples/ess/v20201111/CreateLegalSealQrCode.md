**Example 1: 获取创建法人章二维码**

获取创建法人章二维码

Input: 

```
tccli ess CreateLegalSealQrCode --cli-unfold-argument  \
    --Operator.UserId yDwfsUUckpsqt647UE6uSrk1ZWhYH56z
```

Output: 
```
{
    "Response": {
        "QrcodeBase64": "xxxxxxxxx",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

