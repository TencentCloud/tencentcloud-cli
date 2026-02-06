**Example 1: 查询插件日志采集配置**

查询插件日志采集配置时调用

Input: 

```
tccli tke DescribeControlPlaneLogs --cli-unfold-argument  \
    --ClusterId cls-kaftesta \
    --ClusterType tke
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "Name": "karpenter",
                "LogLevel": 2,
                "LogSetId": "2912eb16-a56c-4b9b-adb0-9828db1ad342",
                "TopicRegion": "ap-guangzhou",
                "TopicId": "2912eb16-a56c-4b9b-adb0-9828db1ad342"
            }
        ],
        "RequestId": "583e6c4b-ff24-42f8-87f1-37e4c00d81b7"
    }
}
```

