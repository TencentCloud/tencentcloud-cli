**Example 1: 正常请求**

正常请求

Input: 

```
tccli tcss CreateAssetImageRegistryScanTask --cli-unfold-argument  \
    --All False \
    --Id 1256299843 \
    --OnlyScanLatest False
```

Output: 
```
{
    "Response": {
        "RequestId": "538366ac-d056-4f69-92ca-cf9bc6c9463b",
        "TaskID": 2
    }
}
```

**Example 2: 镜像仓库创建镜像扫描任务**

镜像仓库创建镜像扫描任务

Input: 

```
tccli tcss CreateAssetImageRegistryScanTask --cli-unfold-argument  \
    --Id 8741110 \
    --ScanType CVE VIRUS RISK
```

Output: 
```
{
    "Response": {
        "RequestId": "68d5d49c-4b6b-46af-b060-46f521db0400"
    }
}
```

