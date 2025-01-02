**Example 1: 集群关联的伸缩组列表**



Input: 

```
tccli tke DescribeClusterAsGroups --cli-unfold-argument  \
    --ClusterId cls-2wds9k9p
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ClusterAsGroupSet": [
            {
                "AutoScalingGroupId": "asg-2wds9k9p",
                "Status": "running",
                "IsUnschedulable": true,
                "Labels": [
                    {
                        "Name": "cluster",
                        "Value": "tke"
                    }
                ],
                "CreatedTime": "2024-05-25 11:00:00"
            }
        ],
        "RequestId": "82f2fe9c-c5fa-4077-9236-f1341180a696"
    }
}
```

