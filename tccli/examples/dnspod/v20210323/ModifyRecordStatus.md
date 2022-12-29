**Example 1: 设置记录状态**

 

Input: 

```
tccli dnspod ModifyRecordStatus --cli-unfold-argument  \
    --Domain dnspod.site \
    --DomainId 62 \
    --RecordId 161 \
    --Status ENABLE
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "RecordId": 161
    }
}
```

