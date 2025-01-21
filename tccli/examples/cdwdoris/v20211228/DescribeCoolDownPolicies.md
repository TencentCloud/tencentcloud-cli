**Example 1: 示例**



Input: 

```
tccli cdwdoris DescribeCoolDownPolicies --cli-unfold-argument  \
    --InstanceId str
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "str",
        "List": [
            {
                "PolicyName": "str",
                "CooldownDatetime": "str",
                "CooldownTtl": "str"
            }
        ],
        "RequestId": "str"
    }
}
```

