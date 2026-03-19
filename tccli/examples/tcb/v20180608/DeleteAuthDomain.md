**Example 1: 删除安全域名**

使用DescribeAuthDomains获取安全域名的id，将想要删除的安全域名的id填入。

Input: 

```
tccli tcb DeleteAuthDomain --cli-unfold-argument  \
    --EnvId envid-xxxxx \
    --DomainIds 61dc0b24-4df6-49ab-9b79-ea611650xxxx
```

Output: 
```
{
    "Response": {
        "Deleted": 1,
        "RequestId": "584b45af-ee33-4dca-a57a-fd60fca92fad"
    }
}
```

