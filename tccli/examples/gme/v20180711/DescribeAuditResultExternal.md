**Example 1: 获审核结果明细（外部API）**



Input: 

```
tccli gme DescribeAuditResultExternal --cli-unfold-argument  \
    --BizId 1500000001 \
    --PageNo 1 \
    --PageSize 10 \
    --BeginTime 1761224396 \
    --EndTime 1761224570 \
    --MinRate 50 \
    --MaxRate 100 \
    --OpenId 10086
```

Output: 
```
{
    "Response": {
        "Data": [],
        "RequestId": "c052505d-d220-4703-bab2-f4766d581322"
    }
}
```

