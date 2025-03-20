**Example 1: 查询安全日志接入对象列表**

查询安全日志接入对象列表

Input: 

```
tccli tcss DescribeSecLogJoinObjectList --cli-unfold-argument  \
    --LogType container_bash \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name Status \
    --Filters.0.Values ONLINE OFFLINE UNINSTALL \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "AutoJoin": false,
        "ExcludedCount": 0,
        "List": [
            {
                "ClusterID": "cls-q0bc0ed2",
                "ClusterMainAddress": "10.0.0.1",
                "ClusterName": "tke2",
                "ClusterStatus": "3",
                "ClusterType": "2",
                "ClusterVersion": "v1.26.1-tke.5",
                "ContainerCnt": 23,
                "HostID": "3b6b1bbc-1c7a-47e2-9ca8-e9c27ec9d068",
                "HostIP": "172.17.1.6",
                "HostName": "tke_cls-q0bc0ed2_worker",
                "HostStatus": "ONLINE",
                "JoinState": true,
                "PublicIP": "159.75.90.217"
            }
        ],
        "RangeType": 1,
        "RequestId": "a38b89a7-fbdf-4133-9981-1c09a5a94895",
        "TotalCount": 55
    }
}
```

