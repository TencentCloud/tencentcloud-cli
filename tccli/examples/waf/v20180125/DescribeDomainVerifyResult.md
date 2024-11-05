**Example 1: 获取域名可添加校验结果**



Input: 

```
tccli waf DescribeDomainVerifyResult --cli-unfold-argument  \
    --Domain randy.qcloudwaf.com \
    --InstanceID waf_in839ad238adsa
```

Output: 
```
{
    "Response": {
        "Msg": "success",
        "VerifyCode": 1,
        "RequestId": "304cb36f-772a-4fdb-9b25-212d8fe5a553"
    }
}
```

