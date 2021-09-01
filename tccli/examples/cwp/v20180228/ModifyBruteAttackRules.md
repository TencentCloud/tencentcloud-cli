**Example 1: 修改爆破阻断模式**



Input: 

```
tccli cwp ModifyBruteAttackRules --cli-unfold-argument  \
    --Rules.0.TimeRange 10 \
    --Rules.0.LoginFailTimes 20 \
    --Rules.1.TimeRange 20 \
    --Rules.1.LoginFailTimes 40
```

Output: 
```
{
    "Response": {
        "RequestId": "c212bdc3-4666-1962-ee24-05e43f5b856c"
    }
}
```

