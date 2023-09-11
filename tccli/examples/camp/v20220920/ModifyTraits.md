**Example 1: 批量修改运维操作**

批量修改运维操作

Input: 

```
tccli camp ModifyTraits --cli-unfold-argument  \
    --ProjectID abc \
    --EnvironmentName abc \
    --ApplicationID abc \
    --InstanceID abc \
    --ComponentName abc \
    --Traits.0.Type volume \
    --Traits.0.Properties.Volume.Objects.0.Name v1 \
    --Traits.0.Properties.Volume.Objects.0.Type CBS \
    --Traits.0.Properties.Volume.Objects.0.CBS.Type CLOUD_SSD \
    --Traits.0.Properties.Volume.Objects.0.CBS.Storage 1 \
    --Traits.0.Properties.Volume.Objects.0.Containers.0.Name c1 \
    --Traits.0.Properties.Volume.Objects.0.Containers.0.MountPath /tmp/c1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

