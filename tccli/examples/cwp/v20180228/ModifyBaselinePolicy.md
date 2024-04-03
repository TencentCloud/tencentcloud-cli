**Example 1: 修改策略**

修改策略

Input: 

```
tccli cwp ModifyBaselinePolicy --cli-unfold-argument  \
    --Data.DetectTime 02:00:00 \
    --Data.PolicyName test1 \
    --Data.DetectInterval 1 \
    --Data.AssetType 0 \
    --Data.IsEnabled 1 \
    --Data.PolicyId 268 \
    --Data.RuleIds 11 \
    --Data.IsDefault 0
```

Output: 
```
{
    "Response": {
        "RequestId": "9549bbb8-915f-4c0c-a03c-5b069d70b4d9"
    }
}
```

**Example 2: 自定义和系统规则添加**

自定义和系统规则添加

Input: 

```
tccli cwp ModifyBaselinePolicy --cli-unfold-argument  \
    --Data.DetectTime 03:00:00 \
    --Data.PolicyName 策略1111 \
    --Data.DetectInterval 1 \
    --Data.AssetType 0 \
    --Data.IsEnabled 1 \
    --Data.PolicyId 1 \
    --Data.RuleIds 4611686018427387909 128
```

Output: 
```
{
    "Response": {
        "RequestId": "07c4d170-f547-4a44-be2e-7f992d483f26"
    }
}
```

