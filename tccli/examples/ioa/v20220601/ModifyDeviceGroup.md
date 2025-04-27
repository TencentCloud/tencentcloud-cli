**Example 1: 测试**

测试

Input: 

```
tccli ioa ModifyDeviceGroup --cli-unfold-argument  \
    --Id 101495 \
    --Name ttt \
    --ParentId 92 \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "7e2bd884-4432-4504-979c-6fa03c56ab1c"
    }
}
```

**Example 2: 修改为配置规则的终端分组**

修改为配置规则的终端分组

Input: 

```
tccli ioa ModifyDeviceGroup --cli-unfold-argument  \
    --DomainInstanceId 1 \
    --Id 104888 \
    --Name test2 \
    --Description 测试描述 \
    --ParentId 101014 \
    --OsType 0 \
    --DivideRules.SimpleRules.0.Expressions.0.Items.0.Key name \
    --DivideRules.SimpleRules.0.Expressions.0.Items.0.Operate 等于 \
    --DivideRules.SimpleRules.0.Expressions.0.Items.0.Value  \
    --DivideRules.SimpleRules.0.Expressions.0.Items.0.Values 44444 55555
```

Output: 
```
{
    "Response": {
        "RequestId": "b1769551-ef56-4a4d-b765-71f236016e9e"
    }
}
```

**Example 3: 有分组规则的示例**

有分组规则的示例

Input: 

```
tccli ioa ModifyDeviceGroup --cli-unfold-argument  \
    --DomainInstanceId 1 \
    --Id 299589 \
    --Name 测试名称-修改 \
    --Description 1 \
    --ParentId 101020 \
    --Locked 0 \
    --OsType 2 \
    --DivideRules.SimpleRules.0.Expressions.0.Items.0.Key name \
    --DivideRules.SimpleRules.0.Expressions.0.Items.0.Operate 等于 \
    --DivideRules.SimpleRules.0.Expressions.0.Items.0.Values 111111111111 222222222mac \
    --DivideRules.SimpleRules.0.Expressions.0.Relation 或者 \
    --DivideRules.SimpleRules.0.Relation 或者 \
    --Priority 30
```

Output: 
```
{
    "Response": {
        "RequestId": "02240971-4244-4750-acec-2250360aade8"
    }
}
```

