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
    "RequestId": "1f2a5c1d-d94b-4296-9b1a-208b237b64da",
    "Result": {
        "TotalCount": 1,
        "Content": [
            {
                "ClusterType": "V",
                "ApplicationType": "V",
                "GroupId": "group-gvklblao",
                "ClusterId": "cluster-by8mnkak",
                "InstanceStatus": "Running",
                "InstanceName": "zeni_2",
                "WanIp": "111.231.188.89",
                "GroupName": "rocketmq-consumer",
                "InstanceId": "ins-0wud1su6",
                "NamespaceId": "namespace-nalpdwyq",
                "VpcId": "vpc-imscnlpv",
                "InstanceAvailableStatus": "Running",
                "ClusterName": "zeni-rocketmq",
                "ApplicationId": "application-maejqev3",
                "ApplicationName": "zeni-rocketmq",
                "NamespaceName": "zeni-rocketmq_default",
                "LanIp": "172.30.0.68"
            }
        ]
    }
}
```

