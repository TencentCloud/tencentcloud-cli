**Example 1: 获取目标节点的有效策略**

获取目标节点的有效策略

Input: 

```
tccli tag DescribeEffectivePolicy --cli-unfold-argument  \
    --TargetId 10001
```

Output: 
```
{
    "Response": {
        "EffectivePolicy": {
            "LastUpdatedTimestamp": 1680239025,
            "PolicyContent": "{\"tags\":{\"Region\":{\"tag_key\":\"Region\",\"tag_value\":[\"ap-guangzhou\"]}}}",
            "TargetId": 100000000000
        },
        "RequestId": "abc"
    }
}
```

