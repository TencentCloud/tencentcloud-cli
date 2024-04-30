**Example 1: DescribeDbTknPwdRules**



Input: 

```
tccli sqlserver DescribeDbTknPwdRules --cli-unfold-argument  \
    --ResourceAccount abc \
    --UserResourceId abc \
    --ResourceRegion abc \
    --InstanceType abc
```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "CharacterType": "abc",
                "Choices": "abc",
                "MinimumLength": 0,
                "MustStart": true
            }
        ],
        "RequiredLength": 0,
        "RequestId": "abc"
    }
}
```

