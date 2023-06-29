**Example 1: 查询恶意请求事件详情**



Input: 

```
tccli otcss DescribeRiskDnsEventDetail --cli-unfold-argument  \
    --EventID 1 \
    --CurrentAppId 1
```

Output: 
```
{
    "Response": {
        "ContainerName": "xx",
        "City": "xx",
        "ProcessAuthority": "xx",
        "ImageID": "xx",
        "ProcessParam": "xx",
        "EventStatus": "xx",
        "LatestFoundTime": "xx",
        "ParentProcessPath": "xx",
        "Description": "xx",
        "ParentProcessUserGroup": "xx",
        "HostName": "xx",
        "ParentProcessParam": "xx",
        "Address": "xx",
        "MatchRuleType": "xx",
        "ParentProcessStartUser": "xx",
        "AncestorProcessStartUser": "xx",
        "OperationTime": "xx",
        "AncestorProcessParam": "xx",
        "Remark": "xx",
        "HostID": "xx",
        "ProcessTree": "xx",
        "ContainerID": "xx",
        "EventCount": 1,
        "Solution": "xx",
        "ProcessUserGroup": "xx",
        "PublicIP": "xx",
        "ImageName": "xx",
        "RequestId": "xx",
        "HostIP": "xx",
        "ProcessStartUser": "xx",
        "EventType": "xx",
        "ContainerNetStatus": "xx",
        "EventID": 1,
        "FeatureLabel": "xx",
        "ContainerStatus": "xx",
        "Reference": [
            "xx"
        ],
        "AncestorProcessUserGroup": "xx",
        "ContainerNetSubStatus": "xx",
        "AncestorProcessPath": "xx",
        "FoundTime": "xx",
        "ProcessPath": "xx",
        "ProcessMd5": "xx",
        "PodName": "xx",
        "ContainerIsolateOperationSrc": "xx"
    }
}
```

