**Example 1: 修改域名解析记录**



Input: 

```
tccli gaap ModifyGlobalDomainDns --cli-unfold-argument  \
    --ProxyIdList 1213 \
    --NationCountryInnerCodes 123 \
    --DnsRecordId 3223 \
    --DomainId xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "19a021f8-dff3-4890-8e7a-ed5054e22e49"
    }
}
```

**Example 2: 修改统一域名的域名解析**



Input: 

```
tccli gaap ModifyGlobalDomainDns --cli-unfold-argument  \
    --ProxyIdList link-4m6fx36h \
    --NationCountryInnerCodes 101001 \
    --DnsRecordId 12756 \
    --DomainId dm-fgsymu39
```

Output: 
```
{
    "Response": {
        "RequestId": "9910da0b-ac6f-4669-bb73-6d0841e93957"
    }
}
```

