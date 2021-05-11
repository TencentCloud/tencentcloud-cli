**Example 1: 更新报警策略状态**



Input: 

```
tccli monitor UpdateAlertRuleState --cli-unfold-argument  \
    --InstanceId my-prom-gg \
    --RuleIds arule-m74lrt6g \
    --RuleState 3
```

Output: 
```
{
    "Response": {
        "RequestId": "ljynf9quqfeko5pwcr24llmhy9rspzye"
    }
}
```

