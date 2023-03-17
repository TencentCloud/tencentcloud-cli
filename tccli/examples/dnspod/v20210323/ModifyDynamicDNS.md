**Example 1: 更新动态 DNS 记录**

 更新动态 DNS 记录

Input: 

```
tccli dnspod ModifyDynamicDNS --cli-unfold-argument  \
    --Domain dnspod.site \
    --DomainId 62 \
    --SubDomain test \
    --RecordId 162 \
    --RecordLine 默认 \
    --RecordLineId 0 \
    --Value 129.23.32.32 \
    --Ttl 600
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "RecordId": 162
    }
}
```

