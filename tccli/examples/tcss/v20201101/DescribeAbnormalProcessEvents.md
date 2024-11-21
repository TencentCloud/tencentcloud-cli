**Example 1: 运行时异常进程列表**

运行时异常进程列表

Input: 

```
tccli tcss DescribeAbnormalProcessEvents --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EventSet": [
            {
                "Behavior": "BEHAVIOR_ALERT",
                "ClusterID": "",
                "ClusterName": "",
                "ContainerId": "2dc265571ad62064781574cb7f854bf25886660c3c99ae677d5c85528409f82d",
                "ContainerIsolateOperationSrc": "",
                "ContainerName": "containner1",
                "ContainerNetStatus": "NORMAL",
                "ContainerNetSubStatus": "NONE",
                "ContainerStatus": "RUNNING",
                "Description": "检测到敏感服务异常子进程启动",
                "EventCount": 51,
                "EventType": "MALICE_PROCESS_START",
                "FoundTime": "2020-10-29 00:05:02",
                "HostID": "8d2fqqq4-8f23-46ba-94ae-da11039e82d3",
                "HostIP": "10.0.86.119",
                "Id": "2961418",
                "ImageId": "sha256:736beeb0cd4edd4e1d3be51d5120eeced04eb50b61fc4a24c54a79ea66e40345",
                "ImageName": "image1",
                "LatestFoundTime": "2020-10-29 23:57:45",
                "MatchAction": "RULE_MODE_ALERT",
                "MatchGroupName": "SYSTEM_DEFINED_RULE",
                "MatchProcessPath": "/bin/bash",
                "MatchRuleId": "100000000000000000000007",
                "MatchRuleLevel": "MIDDLE",
                "MatchRuleName": "ABNORMAL_CHILD_PROC",
                "NodeID": "",
                "NodeName": "qsh4-k8s-sh-prod4-202206287zr4r-47",
                "NodeType": "NORMAL",
                "NodeUniqueID": "d41d8cd98f00b204e9800998ecf8427e",
                "PodIP": "",
                "PodName": "",
                "ProcessPath": "/bin/bash",
                "PublicIP": "",
                "RuleExist": true,
                "RuleId": "111111111111111111111111",
                "Solution": "排查是否为正常业务需要的命令执行,",
                "Status": "EVENT_UNDEAL"
            }
        ],
        "RequestId": "e8a7b8e9-1894-4715-9201-67e0f74692db",
        "TotalCount": 1000
    }
}
```

