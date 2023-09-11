**Example 1: 查询按量计费超级节点资源信息**

查询集群内所有按量计费超级节点资源

Input: 

```
tccli tke DescribePostNodeResources --cli-unfold-argument  \
    --ClusterId cls-0nki77pa
```

Output: 
```
{
    "Response": {
        "PodSet": [
            {
                "Cpu": 0.25,
                "Gpu": 0,
                "Memory": 0.5,
                "NodeName": "eklet-subnet-r5yx1t9w-o155cxns",
                "Num": 1
            }
        ],
        "RequestId": "6b806a51-fea7-4928-9e91-8d7cbb4680ca",
        "ReservedInstanceSet": [
            {
                "Cpu": 2,
                "Gpu": 1,
                "Memory": 2,
                "NodeName": "eklet-subnet-0j105iya",
                "Num": 2
            }
        ]
    }
}
```

