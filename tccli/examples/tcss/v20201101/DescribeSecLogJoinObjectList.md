**Example 1: 查询安全日志接入对象列表**

查询安全日志接入对象列表

Input: 

```
tccli tcss DescribeSecLogJoinObjectList --cli-unfold-argument  \
    --LogType abc \
    --Limit 1 \
    --Offset 1 \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.ExactMatch True \
    --By abc \
    --Order abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "HostID": "abc",
                "HostName": "abc",
                "HostIP": "abc",
                "HostStatus": "abc",
                "ClusterID": "abc",
                "ClusterName": "abc",
                "PublicIP": "abc",
                "JoinState": true,
                "ClusterVersion": "abc",
                "ClusterMainAddress": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

