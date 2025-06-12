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
                    "ApplicationType": "",
                    "GroupId": "group-id",
                    "ClusterId": "cluster-xxxxxx",
                    "InstanceStatus": "Running",
                    "InstanceName": "tsf自动化拨测",
                    "WanIp": "",
                    "GroupName": "name",
                    "InstanceId": "ins-xxxxxx",
                    "NamespaceId": "nid",
                    "VpcId": "vpc-xxxxxx",
                    "InstanceAvailableStatus": "",
                    "ClusterName": "tsf-auto-dialtest",
                    "ApplicationId": "application-id",
                    "ApplicationName": "app-name",
                    "NamespaceName": "namespace-name",
                    "LanIp": "10.0.2.4"
                }
            ]
        }
    }
}
```

