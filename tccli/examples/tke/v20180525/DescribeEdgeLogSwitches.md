**Example 1: 查询开关列表接口示例**



Input: 

```
tccli tke DescribeEdgeLogSwitches --cli-unfold-argument  \
    --ClusterIds cls-xxx1 cls-xxx2
```

Output: 
```
{
    "Response": {
        "SwitchSet": [
            {
                "ClusterId": "cls-xxx1",
                "Audit": {
                    "Enable": true,
                    "TopicSet": "xxxxx",
                    "TopicId": "xxxxx"
                },
                "Event": {
                    "Enable": true,
                    "TopicSet": "xxxxx",
                    "TopicId": "xxxxx"
                },
                "Log": {
                    "Enable": true,
                    "TopicSet": "xxxxx",
                    "TopicId": "xxxxx"
                }
            },
            {
                "ClusterId": "cls-xxx2",
                "Audit": {
                    "Enable": true,
                    "TopicSet": "xxxxx",
                    "TopicId": "xxxxx"
                },
                "Event": {
                    "Enable": true,
                    "TopicSet": "xxxxx",
                    "TopicId": "xxxxx"
                },
                "Log": {
                    "Enable": true,
                    "TopicSet": "xxxxx",
                    "TopicId": "xxxxx"
                }
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

