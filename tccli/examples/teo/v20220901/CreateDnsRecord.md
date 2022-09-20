**Example 1: 创建 DNS 记录**



Input: 

```
tccli teo CreateDnsRecord --cli-unfold-argument  \
    --Priority 1 \
    --Name www.example.com \
    --ZoneId zone-225qgrnvbi9w \
    --Content 1.2.3.4 \
    --Mode dns \
    --TTL 300 \
    --Type A
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "DnsRecordId": "record-225rcy8bw85g"
    }
}
```

