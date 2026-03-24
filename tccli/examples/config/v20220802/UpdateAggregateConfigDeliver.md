**Example 1: 编辑投递设置**



Input: 

```
tccli config UpdateAggregateConfigDeliver --cli-unfold-argument  \
    --Status 1 \
    --DeliverName 投递服务1 \
    --AccountGroupId ca-sdfs7734h24 \
    --DeliverPrefix clonfig_fix \
    --TargetArn qcs::cos:ap-nanjing:100020812189:prefix/1307051190/adad-adasd \
    --DeliverUin 0
```

Output: 
```
{
    "Response": {
        "RequestId": "da85d5e2-4432-4f02-9863-0ab07adeff33"
    }
}
```

