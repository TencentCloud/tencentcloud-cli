**Example 1: 镜像仓库创建镜像一键扫描任务**

镜像仓库创建镜像一键扫描任务

Input: 

```
tccli tcss CreateAssetImageRegistryScanTaskOneKey --cli-unfold-argument  \
    --All True \
    --ScanType CVE RISK
```

Output: 
```
{
    "Response": {
        "RequestId": "68d5d49c-4b6b-46af-b060-46f521db0400"
    }
}
```

