**Example 1: 创建过滤规则**



Input: 

```
tccli eb CreateRule --cli-unfold-argument  \
    --EventBusId eb-anao4i7q \
    --Description rule-test1 \
    --Enable True \
    --EventPattern {
  "source": [
    "ckafka.cloud.tencent"
  ]
} \
    --RuleName rule-test1
```

Output: 
```
{
    "Response": {
        "RuleId": "rule-xxxxxxx",
        "RequestId": "xxxxxxxxxxxxxxxxxxx"
    }
}
```

