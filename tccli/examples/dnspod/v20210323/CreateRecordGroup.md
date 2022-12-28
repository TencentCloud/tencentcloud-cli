**Example 1: 添加记录分组**

 

Input: 

```
tccli dnspod CreateRecordGroup --cli-unfold-argument  \
    --Domain domain.com \
    --GroupName 分组2
```

Output: 
```
{
    "Response": {
        "RequestId": "ec8949ba-ec3c-446e-b9eb-5aeafa238f0a",
        "GroupId": 146
    }
}
```

