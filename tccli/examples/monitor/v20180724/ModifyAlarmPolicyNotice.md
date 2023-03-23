**Example 1: 修改告警策略绑定的告警通知模板**

修改告警策略（policy-asgh3gb2）绑定的告警通知模板

Input: 

```
tccli monitor ModifyAlarmPolicyNotice --cli-unfold-argument  \
    --Module monitor \
    --PolicyId policy-asgh3gb2 \
    --NoticeIds notice-bv9b4ghqbg notice-gj2n9wnt29
```

Output: 
```
{
    "Response": {
        "RequestId": "29ghj2hh-45-h53h234h-23"
    }
}
```

