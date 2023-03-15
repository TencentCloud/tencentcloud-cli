**Example 1: 设置记录备注**

设置记录备注

Input: 

```
tccli dnspod DescribeRecordExistExceptDefaultNS --cli-unfold-argument  \
    --Domain dnspod.site \
    --DomainId 62
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "Exist": true
    }
}
```

