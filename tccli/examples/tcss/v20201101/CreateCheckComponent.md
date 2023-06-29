**Example 1: 安装检查组件示例**



Input: 

```
tccli tcss CreateCheckComponent --cli-unfold-argument  \
    --ClusterInfoList.0.ClusterId cls-0zmsjvko \
    --ClusterInfoList.0.ClusterRegion ap-guangzho
```

Output: 
```
{
    "Response": {
        "RequestId": "feb3881a-be8a-4f43-a485-fa1af264c2cc",
        "InstallResult": "InstallSucc"
    }
}
```

