**Example 1: 批量修改域名递归解析加速状态**



Input: 

```
tccli dnspod ModifyDomainRecursiveStatusBatch --cli-unfold-argument  \
    --DomainList dnspod.com dnspod.cn \
    --Status enable
```

Output: 
```
{
    "Response": {
        "RequestId": "ff6e1e46-2a6e-4290-bb45-f71379938209",
        "JobId": 1817425
    }
}
```

