**Example 1: 修改告警策略基本信息**

修改告警策略 policy-298gn92 的策略名称为“新的云服务器告警策略”

Input: 

```
tccli monitor ModifyAlarmPolicyInfo --cli-unfold-argument  \
    --Module monitor \
    --PolicyId policy-298gn92 \
    --Key NAME \
    --Value 新的云服务器告警策略
```

Output: 
```
{
    "Response": {
        "RequestId": "29ghj2hh-45-h53h234h-23"
    }
}
```

