**Example 1: 验证域名解析**



Input: 

```
tccli vod VerifyDomainRecord --cli-unfold-argument  \
    --Domain abc.com \
    --VerifyType dns
```

Output: 
```
{
    "Response": {
        "RequestId": "30cca198-d096-43ae-8aec-9f87d5a0860e",
        "Result": true
    }
}
```

