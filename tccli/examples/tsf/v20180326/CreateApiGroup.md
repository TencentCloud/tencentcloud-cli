**Example 1: 创建API分组**



Input: 

```
tccli tsf CreateApiGroup --cli-unfold-argument  \
    --GroupName zuul_test_group \
    --GroupContext %2Fuser \
    --AuthType none \
    --Description test \
    --NamespaceNameKey TSF-NamespaceName \
    --ServiceNameKey TSF-ServiceName \
    --NamespaceNameKeyPosition path \
    --ServiceNameKeyPosition path
```

Output: 
```
{
    "Response": {
        "RequestId": "5d996e05507e42d5970cd2e25ed5267a",
        "Result": "grp-12345678"
    }
}
```

