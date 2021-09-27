**Example 1: 查看容器托管的所有服务**



Input: 

```
tccli tcb DescribeCloudBaseRunAllVpcs --cli-unfold-argument  \
    --EnvId lotestapi100004
```

Output: 
```
{
    "Response": {
        "Vpcs": [
            "vpcid-aa",
            "vpcid=bb"
        ],
        "RequestId": "5620b49e-a25a-4007-84ef-03c9035c584d"
    }
}
```

