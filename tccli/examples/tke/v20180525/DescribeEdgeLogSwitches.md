**Example 1: 查询开关列表接口示例**

边缘集群日志开关

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
                "ClusterId": "cls-xxx2",
                "Audit": {
                    "Enable": true,
                    "TopicSet": "a0cd4067-c9a1-a895-907d-03b4025e4f2c",
                    "TopicId": "sadfssfasdf-c9a1-a895-907d-03b4025e4f2c"
                },
                "Event": {
                    "Enable": true,
                    "TopicSet": "sadfssfasdf-564f-a895-907d-03b4025e4f2c",
                    "TopicId": "sadfssfasdf-564f-a895-907d-5465tdtewrt"
                },
                "Log": {
                    "Enable": true,
                    "TopicSet": "3465345-564f-a895-907d-03b4025e4f2c",
                    "TopicId": "6750000-564f-a895-907d-03b4025e4f2c"
                }
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

