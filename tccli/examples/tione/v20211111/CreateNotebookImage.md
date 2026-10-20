**Example 1: 保存镜像示例**

保存镜像示例

Input: 

```
tccli tione CreateNotebookImage --cli-unfold-argument  \
    --Kernels  \
    --ImageInfo.ImageType  \
    --ImageInfo.ImageUrl  \
    --ImageInfo.RegistryRegion  \
    --ImageInfo.RegistryId  \
    --ImageInfo.AllowSaveAllContent True \
    --NotebookId 
```

Output: 
```
{
    "Response": {
        "RequestId": ""
    }
}
```

