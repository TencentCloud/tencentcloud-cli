**Example 1: 修改记录分组**

 

Input: 

```
tccli dnspod ModifyRecordGroup --cli-unfold-argument  \
    --Domain domain.com \
    --GroupName 分组2 \
    --GroupId 145
```

Output: 
```
{
    "Response": {
        "RequestId": "ec8949ba-ec3c-446e-b9eb-5aeafa238f0a",
        "GroupId": 145
    }
}
```

