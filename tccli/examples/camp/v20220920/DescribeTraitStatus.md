**Example 1: 查询运维操作状态**

查询运维操作状态

Input: 

```
tccli camp DescribeTraitStatus --cli-unfold-argument  \
    --ProjectID abc \
    --ApplicationID abc \
    --InstanceID abc \
    --EnvironmentName abc \
    --ComponentName abc \
    --TraitName abc
```

Output: 
```
{
    "Response": {
        "TraitStatus": {
            "Name": "abc",
            "Complete": true
        },
        "RequestId": "abc"
    }
}
```

