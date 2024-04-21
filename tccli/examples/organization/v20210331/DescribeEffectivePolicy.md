**Example 1: 查询目标关联的有效策略**

查询目标关联的有效策略

Input: 

```
tccli organization DescribeEffectivePolicy --cli-unfold-argument  \
    --TargetId 111111111111
```

Output: 
```
{
    "Response": {
        "EffectivePolicy": {
            "TargetId": 111111111111,
            "PolicyContent": "{\"tags\":{\"aaa\":{\"tag_key\":\"aaa\",\"tag_value\":[\"111\",\"222\"],\"resource_type_scope\":[\"cvm:instance\",\"cvm:volume\",\"cvm:keypair\",\"cvm:image\"]},\"bbb\":{\"tag_key\":\"bbb\",\"tag_value\":[\"333\"]}}}",
            "LastUpdatedTimestamp": 1668394639
        },
        "RequestId": "b46d2afe-6893-4529-bc96-2c82d9214957"
    }
}
```

