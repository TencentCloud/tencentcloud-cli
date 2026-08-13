**Example 1: 编辑账号组**

编辑账号组

Input: 

```
tccli config UpdateAggregator --cli-unfold-argument  \
    --OwnerUin 234234 \
    --Description 账号组描述 \
    --AccountGroupId ca-accountGroupNo1 \
    --Name 账号组名称 \
    --AggregatorAccounts.0.MemberUin 110000000001 \
    --AggregatorAccounts.0.MemberName test124 \
    --AggregatorAccounts.1.MemberUin 110000000002 \
    --AggregatorAccounts.1.MemberName test_ckafka
```

Output: 
```
{
    "Response": {
        "RequestId": "da85d5e2-4432-4f02-9863-0ab07adeff33"
    }
}
```

