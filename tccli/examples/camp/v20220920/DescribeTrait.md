**Example 1: 查询 Trait 信息**

查询 Trait 信息

Input: 

```
tccli camp DescribeTrait --cli-unfold-argument  \
    --ProjectID abc \
    --ApplicationID abc \
    --InstanceID abc \
    --EnvironmentName abc \
    --ComponentName abc \
    --TraitName abc \
    --TraitType abc
```

Output: 
```
{
    "Response": {
        "Trait": {
            "Name": "app-v1",
            "Type": "polaris",
            "Properties": {
                "Polaris": {}
            }
        },
        "RequestId": "bitliu-rid-xxxxx"
    }
}
```

