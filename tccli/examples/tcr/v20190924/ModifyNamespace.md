**Example 1: 更新命名空间信息**

用于更新命名空间信息

Input: 

```
tccli tcr ModifyNamespace --cli-unfold-argument  \
    --RegistryId tcr-lfhgf4d3 \
    --NamespaceName nginx \
    --IsPublic False \
    --TagSpecification.ResourceType namespace \
    --TagSpecification.Tags.0.Key tcr \
    --TagSpecification.Tags.0.Value development
```

Output: 
```
{
    "Response": {
        "RequestId": "47871759-7155-41f6-bba3-0bc195a43791"
    }
}
```

