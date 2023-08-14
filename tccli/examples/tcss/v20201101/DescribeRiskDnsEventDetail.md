**Example 1: 查询恶意请求事件详情**

查询恶意请求事件详情

Input: 

```
tccli tcss DescribeRiskDnsEventDetail --cli-unfold-argument  \
    --EventID 1
```

Output: 
```
{
    "Response": {
        "EventID": 1,
        "EventType": "abc",
        "EventCount": 1,
        "FoundTime": "abc",
        "LatestFoundTime": "abc",
        "ContainerID": "abc",
        "ContainerName": "abc",
        "ContainerNetStatus": "abc",
        "ContainerStatus": "abc",
        "ContainerNetSubStatus": "abc",
        "ContainerIsolateOperationSrc": "abc",
        "ImageID": "abc",
        "ImageName": "abc",
        "HostName": "abc",
        "HostIP": "abc",
        "PublicIP": "abc",
        "PodName": "abc",
        "Description": "abc",
        "Solution": "abc",
        "Reference": [
            "abc"
        ],
        "Address": "abc",
        "City": "abc",
        "MatchRuleType": "abc",
        "FeatureLabel": "abc",
        "ProcessAuthority": "abc",
        "ProcessMd5": "abc",
        "ProcessStartUser": "abc",
        "ProcessUserGroup": "abc",
        "ProcessPath": "abc",
        "ProcessTree": "abc",
        "ProcessParam": "abc",
        "ParentProcessStartUser": "abc",
        "ParentProcessUserGroup": "abc",
        "ParentProcessPath": "abc",
        "ParentProcessParam": "abc",
        "AncestorProcessStartUser": "abc",
        "AncestorProcessUserGroup": "abc",
        "AncestorProcessPath": "abc",
        "AncestorProcessParam": "abc",
        "HostID": "abc",
        "EventStatus": "abc",
        "OperationTime": "abc",
        "Remark": "abc",
        "NodeType": "abc",
        "NodeName": "abc",
        "NodeSubNetID": "abc",
        "NodeSubNetName": "abc",
        "NodeSubNetCIDR": "abc",
        "ClusterID": "abc",
        "PodIP": "abc",
        "PodStatus": "abc",
        "NodeUniqueID": "abc",
        "NodeID": "abc",
        "ClusterName": "abc",
        "RequestId": "abc"
    }
}
```

