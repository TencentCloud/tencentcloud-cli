**Example 1: 修改实例**

修改实例

Input: 

```
tccli camp ModifyInstance --cli-unfold-argument  \
    --Platform abc \
    --ProjectID abc \
    --EnvironmentName abc \
    --ApplicationID abc \
    --InstanceID abc \
    --Policies.0.Name abc \
    --Policies.0.Type abc \
    --Policies.0.Properties.Placement.Type abc \
    --Policies.0.Properties.Placement.Region abc \
    --Policies.0.Properties.Placement.Zones.0.Zone abc \
    --Policies.0.Properties.Placement.Zones.0.Weight 0 \
    --Policies.0.Properties.Placement.Components abc \
    --Policies.0.Properties.Placement.Strategy abc \
    --ReadOnly True
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

