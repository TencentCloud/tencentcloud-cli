**Example 1: 修改解析记录**

修改解析记录

Input: 

```
tccli lighthouse ModifyDNSRecord --cli-unfold-argument  \
    --RecordValue 2.3.4.5 \
    --ResourceType INSTANCE \
    --ResourceKey lhins-abcd2345 \
    --RecordId lhdr-dvxu5wn6 \
    --ResourceRegion ap-guangzho \
    --Subdomain www \
    --RecordType A
```

Output: 
```
{
    "Response": {
        "RequestId": "7612faba-597a-4a69-8294-702ad67229a1"
    }
}
```

