**Example 1: 获取域名可添加校验结果**



Input: 

```
tccli waf DescribeDomainVerifyResult --cli-unfold-argument  \
    --Domain test1.qcloud.com \
    --InstanceID aaaaa
```

Output: 
```
{
    "Response": {
        "Msg": "xx",
        "VerifyCode": 1,
        "RequestId": "xx"
    }
}
```

