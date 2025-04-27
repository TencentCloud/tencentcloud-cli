**Example 1: 测试**

测试

Input: 

```
tccli ioa CreateDeviceGroup --cli-unfold-argument  \
    --Name 测试测试 \
    --ParentId 92 \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "642c98ae-2e11-4326-b099-6cd4ec4577f8"
    }
}
```

**Example 2: 配置了分组规则的请求**

配置了分组规则的请求

Input: 

```
tccli ioa CreateDeviceGroup --cli-unfold-argument  \
    --DomainInstanceId 1 \
    --Name 测试 \
    --Description 测试 \
    --ParentId 101014 \
    --OsType 0 \
    --DivideRules.SimpleRules.0.Expressions.0.Items.0.Key name \
    --DivideRules.SimpleRules.0.Expressions.0.Items.0.Operate 等于 \
    --DivideRules.SimpleRules.0.Expressions.0.Items.0.Values 111111111111 222222222 \
    --DivideRules.SimpleRules.0.Expressions.0.Relation 或者 \
    --DivideRules.SimpleRules.0.Relation 或者
```

Output: 
```
{
    "Response": {
        "RequestId": "81543e06-ea80-4084-9c4a-7e89a4216fc7"
    }
}
```

**Example 3: 有分组规则的示例**

有分组规则的示例

Input: 

```
tccli ioa CreateDeviceGroup --cli-unfold-argument  \
    --DomainInstanceId 1 \
    --Name 测试名称 \
    --Description 测试 \
    --ParentId 101020 \
    --Locked 0 \
    --OsType 2 \
    --DivideRules.SimpleRules.0.Expressions.0.Items.0.Key name \
    --DivideRules.SimpleRules.0.Expressions.0.Items.0.Operate 等于 \
    --DivideRules.SimpleRules.0.Expressions.0.Items.0.Values 111111111111 222222222mac \
    --DivideRules.SimpleRules.0.Expressions.0.Relation 或者 \
    --DivideRules.SimpleRules.0.Relation 或者 \
    --Priority 20
```

Output: 
```
{
    "Response": {
        "RequestId": "c71dea82-5bcb-4dc3-b3dd-0bbed364c469"
    }
}
```

