**Example 1: 获取创建法人章二维码**

获取创建法人章二维码

Input: 

```
tccli essbasic CreateLegalSealQrCode --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.AppId yDwfwUUgygormhg1UuS2eARxjMT0mxAw
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

