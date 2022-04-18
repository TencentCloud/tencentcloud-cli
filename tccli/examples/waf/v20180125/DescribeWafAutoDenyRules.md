**Example 1: 获取ip惩罚详细信息**



Input: 

```
tccli waf DescribeWafAutoDenyRules --cli-unfold-argument  \
    --Domain test.qcloudwaf.com
```

Output: 
```
{
    "Response": {
        "TimeThreshold": 0,
        "DenyTimeThreshold": 0,
        "AttackThreshold": 0,
        "DefenseStatus": 0,
        "RequestId": "xx"
    }
}
```

