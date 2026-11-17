**Example 1: 修改GPU资源组名称**

仅同步修改当前租户 GPU 资源组的名称，允许重名、同名重试；不修改规格、数量、计费期限或续费标记。不存在或不属于当前租户的资源组返回 ResourceNotFound。

Input: 

```
tccli ags ModifyGPUResourceGroup --cli-unfold-argument  \
    --ResourceGroupId gpug-example \
    --Name 新的推理服务组
```

Output: 
```
{
    "Response": {
        "RequestId": "request-example"
    }
}
```

