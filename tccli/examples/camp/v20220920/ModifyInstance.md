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

**Example 2: modifyinstance修改实例**



Input: 

```
tccli camp ModifyInstance --cli-unfold-argument  \
    --ProjectID prj-xxxxxxx \
    --ApplicationID app-xxxxxx \
    --InstanceID tad-xxxxxxx \
    --EnvironmentName development \
    --CMDBAdmins.0.Tencent.Name aaaaa \
    --CMDBAdmins.1.Tencent.Name def \
    --CMDBAdmins.2.Tencent.Name abvc \
    --CMDBAdmins.3.Tencent.Name adasdas1
```

Output: 
```
{
    "Response": {
        "RequestId": "26ccfdd8-6d24-4236-9321-58d0467da44f"
    }
}
```

