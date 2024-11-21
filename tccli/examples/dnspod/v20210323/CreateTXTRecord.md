**Example 1: 添加TXT记录**

添加TXT记录

Input: 

```
tccli dnspod CreateTXTRecord --cli-unfold-argument  \
    --Domain 1777.cn \
    --RecordLine 默认 \
    --Value 43045375 \
    --TTL 600 \
    --Status ENABLE
```

Output: 
```
{
    "Response": {
        "RecordId": 16412959,
        "RequestId": "5fc6eba2-3a28-41da-b3c6-70b8e55c447e"
    }
}
```

