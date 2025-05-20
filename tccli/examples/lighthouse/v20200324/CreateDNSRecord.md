**Example 1: 新增域名解析记录**

用户对指定域名新增一条解析记录

Input: 

```
tccli lighthouse CreateDNSRecord --cli-unfold-argument  \
    --DomainId lhdo-b9h9nda1 \
    --Record.Subdomain abc \
    --Record.RecordType A \
    --Record.RecordValue 192.168.1.1 \
    --Record.ResourceType INSTANCE \
    --Record.ResourceKey lhins-abcd1234 \
    --Record.ResourceRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RecordId": "lhdr-abcd1234",
        "RequestId": "eaebb8c7-beda-4233-a66£-769c020g568"
    }
}
```

