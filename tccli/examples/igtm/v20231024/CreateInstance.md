**Example 1: 创建免费版套餐**

创建免费版套餐

Input: 

```
tccli igtm CreateInstance --cli-unfold-argument  \
    --InstanceName example-test-instance \
    --Domain igtm.example.com \
    --AccessType custom \
    --AccessDomain example.com \
    --AccessSubDomain access.igtm \
    --GlobalTtl 300 \
    --PackageType Free \
    --Remark 测试实例
```

Output: 
```
{
    "Response": {
        "RequestId": "ec040ddf-7c7d-4aef-9e0d-6f3105fa0a4c"
    }
}
```

