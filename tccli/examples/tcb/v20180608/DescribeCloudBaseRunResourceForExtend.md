**Example 1: 查看容器托管的资源状态**



Input: 

```
tccli tcb DescribeCloudBaseRunResourceForExtend --cli-unfold-argument  \
    --EnvId lotestapi100004
```

Output: 
```
{
    "Response": {
        "ClusterStatus": "succ",
        "VirtualClusterId": "cjd123",
        "RequestId": "5620b49e-a25a-4007-84ef-03c9035c584d",
        "VpcId": "xx",
        "SubnetIds": [
            {
                "Target": "xx",
                "Zone": "xx",
                "Region": "xx",
                "Cidr": "xx",
                "Type": "xx",
                "Id": "xx",
                "Name": "xx"
            }
        ],
        "Region": "xx"
    }
}
```

