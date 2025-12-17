**Example 1: 创建统一元数据管理实例**

创建统一元数据管理实例

Input: 

```
tccli tccatalog CreateMetastoreInstance --cli-unfold-argument  \
    --ProductId 64 \
    --Size free \
    --DisplayName jack \
    --OwnerDisplayName bob
```

Output: 
```
{
    "Response": {
        "RequestId": "d830face-6587-4263-8ab0-56bda2657xxx",
        "InstanceId": "tcc-xxxxxxxx"
    }
}
```

