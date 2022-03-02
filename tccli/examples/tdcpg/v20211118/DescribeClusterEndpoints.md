**Example 1: 查询集群接入点**



Input: 

```
tccli tdcpg DescribeClusterEndpoints --cli-unfold-argument  \
    --ClusterId tdcpg-xx
```

Output: 
```
{
    "Response": {
        "EndpointSet": [
            {
                "ClusterId": "tdcpg-77iesdqa",
                "EndpointId": "tdcpg-ep-6c6xs52r",
                "EndpointName": "tdcpg-ep-6c6xs52r",
                "EndpointType": "RW",
                "PrivateIp": "10.0.64.20",
                "PrivatePort": 5432,
                "SubnetId": "subnet-5wnhtsmw",
                "VpcId": "vpc-l0ee2prd",
                "WanDomain": "",
                "WanIp": "",
                "WanPort": 0
            },
            {
                "ClusterId": "tdcpg-77iesdqa",
                "EndpointId": "tdcpg-ep-ffscxj6f",
                "EndpointName": "tdcpg-ep-ffscxj6f",
                "EndpointType": "RO",
                "PrivateIp": "10.0.64.24",
                "PrivatePort": 5432,
                "SubnetId": "subnet-5wnhtsmw",
                "VpcId": "vpc-l0ee2prd",
                "WanDomain": "",
                "WanIp": "",
                "WanPort": 0
            }
        ],
        "RequestId": "d355225a-3ac6-4ef0-a606-feab5d8a45c0",
        "TotalCount": 2
    }
}
```

