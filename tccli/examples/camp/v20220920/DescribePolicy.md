**Example 1: 查询策略**

查询策略

Input: 

```
tccli camp DescribePolicy --cli-unfold-argument  \
    --ProjectID abc \
    --ApplicationID abc \
    --InstanceID abc \
    --EnvironmentName abc \
    --PolicyName abc
```

Output: 
```
{
    "Response": {
        "Policy": {
            "Name": "abc",
            "Type": "abc",
            "Properties": {
                "Placement": {
                    "Type": "abc",
                    "Region": "abc",
                    "Zones": [
                        {
                            "Zone": "abc",
                            "Weight": 0
                        }
                    ],
                    "Components": [
                        "abc"
                    ],
                    "Strategy": "abc",
                    "Selector": [
                        {
                            "Key": "abc",
                            "Value": "abc"
                        }
                    ]
                }
            }
        },
        "RequestId": "abc"
    }
}
```

