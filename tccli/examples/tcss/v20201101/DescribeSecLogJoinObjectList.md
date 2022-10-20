**Example 1: 查询安全日志接入对象列表**



Input: 

```
tccli tcss DescribeSecLogJoinObjectList --cli-unfold-argument  \
    --By xx \
    --LogType container_bash \
    --Limit 1 \
    --Filters.0.Values UNINSTALL \
    --Filters.0.Name HostState \
    --Filters.0.ExactMatch True \
    --Offset 1 \
    --Order asc
```

Output: 
```
{
    "Response": {
        "TotalCount": 15,
        "List": [
            {
                "ClusterMainAddress": "xx",
                "HostID": "xx",
                "ClusterVersion": "xx",
                "ClusterName": "xx",
                "HostName": "xx",
                "ClusterID": "xx",
                "PublicIP": "xx",
                "JoinState": true,
                "HostIP": "xx",
                "HostStatus": "xx"
            }
        ],
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

