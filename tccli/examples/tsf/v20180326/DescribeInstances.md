**Example 1: 查询机器列表**



Input: 

```
tccli tsf DescribeInstances --cli-unfold-argument  \
    --Filters.0.Name name \
    --Filters.0.Values pepy zeni
```

Output: 
```
{
    "Response": {
        "RequestId": "d2de5f06-bc71-4bd5-aa93-1188ce24aa46",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "ClusterType": "V",
                    "ApplicationType": null,
                    "GroupId": null,
                    "ClusterId": "cluster-xxxxxx",
                    "InstanceStatus": "Running",
                    "InstanceName": "tsf自动化拨测",
                    "WanIp": null,
                    "GroupName": null,
                    "InstanceId": "ins-xxxxxx",
                    "NamespaceId": null,
                    "VpcId": "vpc-xxxxxx",
                    "InstanceAvailableStatus": null,
                    "ClusterName": "tsf-auto-dialtest",
                    "ApplicationId": null,
                    "ApplicationName": null,
                    "NamespaceName": null,
                    "LanIp": "10.0.2.4"
                }
            ]
        }
    }
}
```

