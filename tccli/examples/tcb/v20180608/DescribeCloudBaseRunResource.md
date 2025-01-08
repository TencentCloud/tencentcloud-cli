**Example 1: 查看容器托管的资源状态**



Input: 

```
tccli tcb DescribeCloudBaseRunResource --cli-unfold-argument  \
    --EnvId lotestapi100004
```

Output: 
```
{
    "Response": {
        "ClusterStatus": "succ",
        "VirtualClusterId": "cjd123",
        "RequestId": "5620b49e-a25a-4007-84ef-03c9035c584d",
        "VpcId": "vpc-sdfs",
        "SubnetIds": [
            {
                "Target": "tar",
                "Zone": "shanghai-z",
                "Region": "ap-shanghai",
                "Cidr": "",
                "Type": "",
                "Id": "subnet-sdf",
                "Name": "djfk"
            }
        ],
        "Region": "ap-shanghai"
    }
}
```

