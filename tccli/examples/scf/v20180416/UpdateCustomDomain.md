**Example 1: 示例1**

更新自定义域名的证书Id,并关闭waf

Input: 

```
tccli scf UpdateCustomDomain --cli-unfold-argument  \
    --Domain www.ccc.com \
    --Protocol HTTP&HTTPS \
    --CertConfig.CertificateId cvvxxJ3DK7 \
    --WafConfig.WafOpen CLOSE \
    --WafConfig.WafInstanceId 
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

