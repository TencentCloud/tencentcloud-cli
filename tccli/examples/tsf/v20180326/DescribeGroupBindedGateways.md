**Example 1: 查询某个API分组已绑定的网关部署组信息列表**



Input: 

```
tccli tsf DescribeGroupBindedGateways --cli-unfold-argument  \
    --GroupId grp-nb08ur29 \
    --SearchWord zuul \
    --Offset 0 \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "RequestId": "f5e456a5-94c9-46d3-96ab-27dd24948da5",
        "Result": {
            "Content": [
                {
                    "ApplicationId": "application-ydopqnxa",
                    "ApplicationName": "shedfree-gw",
                    "ApplicationType": "V",
                    "ClusterType": "V",
                    "DeployGroupId": "group-yd3b588a",
                    "DeployGroupName": "shed-zuul-1",
                    "GroupStatus": "Running"
                },
                {
                    "ApplicationId": "application-ydopqnxa",
                    "ApplicationName": "shedfree-gw",
                    "ApplicationType": "V",
                    "ClusterType": "V",
                    "DeployGroupId": "group-yq9d6wev",
                    "DeployGroupName": "shed-zuul-3",
                    "GroupStatus": "Running"
                },
                {
                    "ApplicationId": "application-ydopqnxa",
                    "ApplicationName": "shedfree-gw",
                    "ApplicationType": "V",
                    "ClusterType": "V",
                    "DeployGroupId": "group-yx87px4a",
                    "DeployGroupName": "shed-zuul-2",
                    "GroupStatus": "Running"
                }
            ],
            "TotalCount": 3
        }
    }
}
```

