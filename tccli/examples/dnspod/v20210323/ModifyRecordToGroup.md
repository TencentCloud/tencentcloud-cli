**Example 1: 将记录添加到分组**

 

Input: 

```
tccli dnspod ModifyRecordToGroup --cli-unfold-argument  \
    --Domain domain.com \
    --GroupId 156 \
    --RecordId 123232|2343232
```

Output: 
```
{
    "Response": {
        "RequestId": "ec8949ba-ec3c-446e-b9eb-5aeafa238f0a"
    }
}
```

