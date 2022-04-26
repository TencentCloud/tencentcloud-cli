**Example 1: 集群关联的伸缩组列表**



Input: 

```
tccli tke DescribeClusterAsGroups --cli-unfold-argument  \
    --ClusterId cls-xxxxxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ClusterAsGroupSet": [
            {
                "AutoScalingGroupId": "xx",
                "Status": "xx",
                "IsUnschedulable": true,
                "Labels": [
                    {
                        "Name": "xx",
                        "Value": "xx"
                    }
                ],
                "CreatedTime": "xx"
            }
        ],
        "RequestId": "82f2fe9c-c5fa-4077-9236-f1341180a696"
    }
}
```

