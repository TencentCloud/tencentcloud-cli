**Example 1: 创建合规检查任务**



Input: 

```
tccli tcss CreateComplianceTask --cli-unfold-argument  \
    --AssetTypeSet ASSET_CONTAINER
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx",
        "TaskId": 12345
    }
}
```

