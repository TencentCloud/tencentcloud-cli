**Example 1: 查询统一集群下实例ID列表**

查询统一集群下实例ID列表

Input: 

```
tccli cynosdb DescribeInstancesWithinSameCluster --cli-unfold-argument  \
    --UniqVpcId abc \
    --Vip abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstanceIds": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

