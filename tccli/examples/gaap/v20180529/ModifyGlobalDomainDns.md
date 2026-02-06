**Example 1: 修改统一域名的域名解析**



Input: 

```
tccli gaap ModifyGlobalDomainDns --cli-unfold-argument  \
    --DnsRecordId 1805447 \
    --DomainId dm-d5zi5hi7 \
    --NationCountryInnerCodes 102001 \
    --ProxyIdList link-mxz3pxo9
```

Output: 
```
{
    "Response": {
        "RequestId": "61c6f09c-669c-412f-b200-f9d9b4b10621"
    }
}
```

