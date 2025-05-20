**Example 1: 修改记录**

 

Input: 

```
tccli dnspod ModifyRecord --cli-unfold-argument  \
    --Domain dnspod.cn \
    --DomainId 62 \
    --SubDomain bbbb \
    --RecordType A \
    --RecordLine 默认 \
    --RecordLineId 0 \
    --Value 129.23.32.32 \
    --MX 0 \
    --TTL 600 \
    --Weight 10 \
    --Status DISABLE \
    --RecordId 162
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

