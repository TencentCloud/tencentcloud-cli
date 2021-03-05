**Example 1: 提交信审申请**



Input: 

```
tccli cr ApplyCreditAudit --cli-unfold-argument  \
    --Module Credit \
    --Operation Apply \
    --InstId ins-xxx \
    --ProductId pdt-yy \
    --CaseId xxx \
    --CallbackUrl aad \
    --Data 123
```

Output: 
```
{
    "Response": {}
}
```

