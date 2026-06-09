**Example 1: 模型删除示例**



Input: 

```
tccli tcr DeleteAIModel --cli-unfold-argument  \
    --RegistryId tcr-kpfrletb \
    --Items.0.NamespaceName ml-models \
    --Items.0.RepositoryName yolov8 \
    --Items.0.Reference v2.0.0
```

Output: 
```
{
    "Response": {
        "RequestId": "09306de4-ff42-485a-83ea-20f88970cf80"
    }
}
```

