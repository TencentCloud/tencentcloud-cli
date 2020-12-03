**Example 1: 查询某个API分组已绑定的网关部署组信息列表**



Input: 

```
tccli tsf DescribeGroupBindedGateways --cli-unfold-argument  \
    --GroupId group-s7j2sk4 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Result": {
            "Content": [
                {
                    "DeployGroupId": "xx",
                    "ApplicationName": "xx",
                    "GroupStatus": "xx",
                    "ClusterType": "xx",
                    "DeployGroupName": "xx",
                    "ApplicationType": "xx",
                    "ApplicationId": "xx"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "xx"
    }
}
```

