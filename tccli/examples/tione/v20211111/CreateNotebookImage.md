**Example 1: 保存镜像示例**

保存镜像示例

Input: 

```
tccli tione CreateNotebookImage --cli-unfold-argument  \
    --Kernels abc \
    --ImageInfo.ImageType abc \
    --ImageInfo.ImageUrl abc \
    --ImageInfo.RegistryRegion abc \
    --ImageInfo.RegistryId abc \
    --ImageInfo.AllowSaveAllContent True \
    --NotebookId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

