**Example 1: 示例1**

创建自定义分组接口

Input: 

```
tccli ioa CreateDeviceVirtualGroup --cli-unfold-argument  \
    --OsType 0 \
    --Description obsolete \
    --DeviceVirtualGroupName auottest1666336897100
```

Output: 
```
{
    "Response": {
        "RequestId": "abc372a3-885d-4c26-815b-799afb0ada55",
        "Data": {
            "Id": 356
        }
    }
}
```

**Example 2: 示例2**

创建终端自定义分组

Input: 

```
tccli ioa CreateDeviceVirtualGroup --cli-unfold-argument  \
    --DeviceVirtualGroupName auto7 \
    --Description 自动分组测试 \
    --OsType 0 \
    --TimeType 3 \
    --AutoMinute 10 \
    --AutoRules.SimpleRules.0.Expressions.0.Items.0.Key mid \
    --AutoRules.SimpleRules.0.Expressions.0.Items.0.Operate 等于 \
    --AutoRules.SimpleRules.0.Expressions.0.Items.0.Value 111111111
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": 9
        },
        "RequestId": "088bd8af-4ff1-448c-8e48-6d4e860df5cc"
    }
}
```

