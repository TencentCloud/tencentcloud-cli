**Example 1: 获取边缘计算集群的当前状态以及过程信息**



Input: 

```
tccli tke DescribeTKEEdgeClusterStatus --cli-unfold-argument  \
    --ClusterId cls-xxxxxx
```

Output: 
```
{
    "Response": {
        "Phase": "Initializing",
        "Conditions": [
            {
                "Type": "初始化Master部署环境",
                "Status": "True",
                "LastProbeTime": "2020-02-25 12:10:15",
                "LastTransitionTime": "2020-02-25 12:10:15",
                "Reason": "WaitingProcess",
                "Message": "waiting process"
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

