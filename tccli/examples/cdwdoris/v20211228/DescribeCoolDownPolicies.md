**Example 1: 示例**



Input: 

```
tccli cdwdoris DescribeCoolDownPolicies --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "List": [
            {
                "PolicyName": "abc",
                "CooldownDatetime": "abc",
                "CooldownTtl": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

