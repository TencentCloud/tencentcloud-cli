**Example 1: 批量修改域名CNAME加速状态**



Input: 

```
tccli dnspod ModifyDomainCNAMESpeedupStatusBatch --cli-unfold-argument  \
    --DomainList dnspod.com dnspod.cn \
    --Status enable
```

Output: 
```
{
    "Response": {
        "RequestId": "b73e095d-87d8-4a4f-b78b-f1aec07202ff",
        "JobId": 1817401
    }
}
```

