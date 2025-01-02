**Example 1: 查询开关列表接口示例**

边缘集群日志开关

Input: 

```
tccli tke DescribeEdgeLogSwitches --cli-unfold-argument  \
    --ClusterIds cls-e55paxnt cls-e55paxnt
```

Output: 
```
{
    "Response": {
        "SwitchSet": [
            "logsetid: 8hhy32hru27"
        ],
        "RequestId": "iu3u89fvfsyr37819hi9"
    }
}
```

