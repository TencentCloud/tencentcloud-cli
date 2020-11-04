**Example 1: 获取一个传统型负载均衡的后端服务信息**



Input: 

```
tccli clb DescribeClassicalLBTargets --cli-unfold-argument  \
    --LoadBalancerId lb-a3u5l5zc
```

Output: 
```
{
    "Response": {
        "Targets": [
            {
                "Type": "CVM",
                "InstanceId": "ins-odjhn6vc",
                "Weight": 30,
                "InstanceName": "vpc02",
                "PrivateIpAddresses": [
                    "10.104.63.53"
                ],
                "PublicIpAddresses": [],
                "RunFlag": 2
            }
        ],
        "RequestId": "1e241bcf-4091-481e-9d81-8c0d01d3f82d"
    }
}
```

