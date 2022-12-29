**Example 1: 设置记录备注**

 

Input: 

```
tccli dnspod ModifyRecordRemark --cli-unfold-argument  \
    --Domain dnspod.site \
    --DomainId 62 \
    --RecordId 162 \
    --Remark 这是解析记录的备注
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166"
    }
}
```

