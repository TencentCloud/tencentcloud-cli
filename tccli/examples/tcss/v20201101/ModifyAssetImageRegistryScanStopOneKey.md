**Example 1: 镜像仓库停止镜像一键扫描任务**

镜像仓库停止镜像一键扫描任务

Input: 

```
tccli tcss ModifyAssetImageRegistryScanStopOneKey --cli-unfold-argument  \
    --All True
```

Output: 
```
{
    "Response": {
        "RequestId": "459ab056-ab0e-460f-b937-9e5c7d02275f"
    }
}
```

**Example 2: 停止任务**

停止任务

Input: 

```
tccli tcss ModifyAssetImageRegistryScanStopOneKey --cli-unfold-argument  \
    --TaskID 13
```

Output: 
```
{
    "Response": {
        "RequestId": "64c2b99b-ed9d-431b-b0c7-15c73d57c8e4"
    }
}
```

