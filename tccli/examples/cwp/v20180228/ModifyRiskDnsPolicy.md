**Example 1: 更改恶意请求策略**



Input: 

```
tccli cwp ModifyRiskDnsPolicy --cli-unfold-argument  \
    --Data.PolicyId 5000001 \
    --Data.PolicyName test \
    --Data.PolicyType 1 \
    --Data.PolicyDesc desc \
    --Data.PolicyAction 1 \
    --Data.HostScope 1 \
    --Data.HostIds a918d8a1-c4c1-4998-80ff-5a60792c93a8 \
    --Data.Domains YS5jb20= \
    --Data.IsEnabled 1 \
    --Data.IsDealOldEvent 1 \
    --Data.UpdateTime 2022-09-19 17:12:01 \
    --Data.EventId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "130e109f-a922-4d16-827d-b17a366125a2"
    }
}
```

