**Example 1: 修改告警策略状态**

将一个策略禁用

Input: 

```
tccli monitor ModifyAlarmPolicyStatus --cli-unfold-argument  \
    --Module monitor \
    --PolicyId policy-2g22g82 \
    --Enable 0
```

Output: 
```
{
    "Response": {
        "RequestId": "29ghj2hh-45-h53h234h-23"
    }
}
```

