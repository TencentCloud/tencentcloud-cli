**Example 1: 创建服务级账号**

创建服务级账号

Input: 

```
tccli tcr CreateServiceAccount --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --Name servie-account3 \
    --Duration 10 \
    --Permissions.0.Resource ns1 \
    --Permissions.0.Actions tcr:PushRepository tcr:PullRepository tcr:CreateRepository tcr:CreateHelmChart tcr:DescribeHelmCharts
```

Output: 
```
{
    "Response": {
        "CreateTime": "2025-01-03T11:00:19+08:00",
        "ExpiresAt": 1736737219170,
        "Name": "tcr$servie-account3",
        "Password": "4NcJarnZibtlj8ViIPKQRNQ0j2IyVG03",
        "RequestId": "13561dff-12b7-4e35-bec0-49f40e13af30"
    }
}
```

**Example 2: 使用Duration创建ServiceAccount**

使用Duration创建ServiceAccount

Input: 

```
tccli tcr CreateServiceAccount --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --Name servie-account4 \
    --Duration 10 \
    --Permissions.0.Resource ns1 \
    --Permissions.0.Actions tcr:PushRepository
```

Output: 
```
{
    "Response": {
        "CreateTime": "2025-01-07T11:48:31+08:00",
        "ExpiresAt": 1737085710747,
        "Name": "tcr$servie-account4",
        "Password": "bVMZuTO6eYFvpZX9sVIxfyA3UHtIUrCa",
        "RequestId": "f63f97d2-f5be-43b5-931e-13c026aba9c7"
    }
}
```

