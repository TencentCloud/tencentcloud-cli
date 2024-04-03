**Example 1: 正常请求**

正常请求

Input: 

```
tccli tcss ModifyAssetImageRegistryScanStop --cli-unfold-argument  \
    --Id 314 \
    --TaskID 2
```

Output: 
```
{
    "Response": {
        "RequestId": "18808687-b25a-43d8-9f79-5541bbe47a8e"
    }
}
```

**Example 2: 镜像仓库停止镜像一键扫描任务**

镜像仓库停止镜像一键扫描任务

Input: 

```
tccli tcss ModifyAssetImageRegistryScanStop --cli-unfold-argument  \
    --Id 12034807
```

Output: 
```
{
    "Response": {
        "RequestId": "459ab056-ab0e-460f-b937-9e5c7d02275f"
    }
}
```

