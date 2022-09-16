**Example 1: 请求示例**



Input: 

```
tccli live AuthenticateDomainOwner --cli-unfold-argument  \
    --VerifyType dnsCheck \
    --DomainName akxynt.cn
```

Output: 
```
{
    "Response": {
        "Content": "cssauth_da06159efa92c365182ba5d453a7b65b",
        "MainDomain": "akxynt.cn",
        "RequestId": "20a9d1c1-7b2a-48b5-9a78-c0bccab3dfb6",
        "Status": 0
    }
}
```

