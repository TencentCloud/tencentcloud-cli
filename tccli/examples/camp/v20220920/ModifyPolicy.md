**Example 1: 修改策略**

修改策略

Input: 

```
tccli camp ModifyPolicy --cli-unfold-argument  \
    --ProjectID abc \
    --EnvironmentName abc \
    --ApplicationID abc \
    --InstanceID abc \
    --Policy.Name abc \
    --Policy.Type abc \
    --Policy.Properties.Placement.Type abc \
    --Policy.Properties.Placement.Region abc \
    --Policy.Properties.Placement.Zones.0.Zone abc \
    --Policy.Properties.Placement.Zones.0.Weight 0 \
    --Policy.Properties.Placement.Components abc \
    --Policy.Properties.Placement.Strategy abc \
    --Policy.Properties.Placement.Selector.0.Key abc \
    --Policy.Properties.Placement.Selector.0.Value abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

