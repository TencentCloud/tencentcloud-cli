**Example 1: 修改 DNS 记录**



Input: 

```
tccli teo ModifyDnsRecord --cli-unfold-argument  \
    --Priority 1 \
    --DnsRecordName a.example.com \
    --ZoneId zone-20hyebgyfsko \
    --Content 1.1.1.1 \
    --Mode dns_only \
    --TTL 600 \
    --DnsRecordType A \
    --DnsRecordId record-21q7frcpseaw
```

Output: 
```
{
    "Response": {
        "RequestId": "015c3e96-2bfd-4171-a25a-a8956a2ad6c0"
    }
}
```

