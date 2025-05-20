**Example 1: 新增域名解析记录**

用户对指定域名新增一条解析记录

Input: 

```
tccli lighthouse CreateDNSRecords --cli-unfold-argument  \
    --DomainId lhdo-b9h9nda1 \
    --Records.0.Subdomain abc \
    --Records.0.RecordType A \
    --Records.0.RecordValue 192.168.1.1 \
    --Records.0.ResourceType INSTANCE \
    --Records.0.ResourceKey lhins-abcd1234 \
    --Records.0.ResourceRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RecordIdSet": [
            "lhdr-abcd1234"
        ],
        "ErrorIndexSet": [],
        "ErrorMessageSet": [],
        "RequestId": "eaebb8c7-beda-4233-a66£-769c020g56a"
    }
}
```

