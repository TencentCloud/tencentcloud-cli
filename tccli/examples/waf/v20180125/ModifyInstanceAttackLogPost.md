**Example 1: 开通实例攻击日志投递**



Input: 

```
tccli waf ModifyInstanceAttackLogPost --cli-unfold-argument  \
    --InstanceId waf_000000001 \
    --AttackLogPost 1
```

Output: 
```
{
    "Response": {
        "RequestId": "b4f13899-561b-46a0-a045-6ba6b72c38f2"
    }
}
```

