**Example 1: 创建镜像扫描任务**



Input: 

```
tccli tcss CreateAssetImageScanTask --cli-unfold-argument  \
    --ScanVirus True \
    --ScanRisk True \
    --ScanVul True \
    --All True
```

Output: 
```
{
    "Response": {
        "RequestId": "a6d8d540-940f-47d9-8d7f-daac832ba5b4",
        "TaskID": "6013a6c334b9a9000cf519be"
    }
}
```

