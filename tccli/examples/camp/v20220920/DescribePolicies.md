**Example 1: 查询策略列表**

查询策略列表

Input: 

```
tccli camp DescribePolicies --cli-unfold-argument  \
    --ProjectID abc \
    --EnvironmentName abc \
    --ApplicationID abc \
    --InstanceID abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.Query abc \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Policies": [
            {
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
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

