**Example 1: 修改弱口令配置**

修改弱口令配置

Input: 

```
tccli cwp ModifyBaselineWeakPassword --cli-unfold-argument  \
    --Data.0.PasswordId 3432 \
    --Data.0.WeakPassword 1111
```

Output: 
```
{
    "Response": {
        "RequestId": "ee20febc-b59d-45ab-97f6-d55efdfa57b7"
    }
}
```

