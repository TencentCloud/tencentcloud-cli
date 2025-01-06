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
    --RegistryId tcr-45uu7ras \
    --Name test \
    --Description for test \
    --Duration 10 \
    --Permissions.0.Resource test \
    --Permissions.0.Actions tcr:PullRepository tcr:PushRepository tcr:CreateRepository
```

Output: 
```
{
    "Response": {
        "CreateTime": "2023-03-28T15:48:31+08:00",
        "ExpiresAt": 1680853711137,
        "Name": "tcr$test",
        "Password": "oNKUtqrB5Eb68JufkVanSwuhmC4Ergn7",
        "RequestId": "20b67612-28a0-4c51-8efb-0fe14bc23a64"
    }
}
```

