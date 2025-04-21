**Example 1: 示例1**

编译自定义分组时使用

Input: 

```
tccli ioa ModifyDeviceVirtualGroup --cli-unfold-argument  \
    --DeviceVirtualGroupId 358 \
    --Description 修改时的详情 \
    --DeviceVirtualGroupName 已修改分组
```

Output: 
```
{
    "Response": {
        "RequestId": "760bbcbc-d717-47e0-864f-1ff5c1653caf"
    }
}
```

**Example 2: 示例2**

修改终端自定义分组

Input: 

```
tccli ioa ModifyDeviceVirtualGroup --cli-unfold-argument  \
    --DeviceVirtualGroupName auto00 \
    --Description xxxxx \
    --DeviceVirtualGroupId 7 \
    --OsType 0 \
    --TimeType 3 \
    --AutoMinute 10 \
    --AutoRules.SimpleRules.0.Expressions.0.Items.0.Key mid \
    --AutoRules.SimpleRules.0.Expressions.0.Items.0.Operate 不包含 \
    --AutoRules.SimpleRules.0.Expressions.0.Items.0.Value 2222111
```

Output: 
```
{
    "Response": {
        "RequestId": "85423269-12f9-48c7-8ead-a5f5b0604555"
    }
}
```

