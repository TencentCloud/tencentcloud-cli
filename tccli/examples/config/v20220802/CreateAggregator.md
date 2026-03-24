**Example 1: 新增账号组**

新增账号组

Input: 

```
tccli config CreateAggregator --cli-unfold-argument  \
    --Type RD \
    --Name 账号组1 \
    --Description 账号组描述 \
    --AggregatorAccounts.0.MemberUin 110000000001 \
    --AggregatorAccounts.0.MemberName test124 \
    --AggregatorAccounts.1.MemberUin 110000000002 \
    --AggregatorAccounts.1.MemberName test_ckafka
```

Output: 
```
{
    "Response": {
        "AccountGroupId": "ca-sdfs7734h24h3",
        "RequestId": "da85d5e2-4432-4f02-9863-0ab07adeff33"
    }
}
```

