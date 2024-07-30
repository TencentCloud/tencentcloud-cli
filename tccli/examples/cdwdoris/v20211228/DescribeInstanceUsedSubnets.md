**Example 1: 获取集群已使用子网信息**



Input: 

```
tccli cdwdoris DescribeInstanceUsedSubnets --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "VpcId": "abc",
        "UsedSubnets": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

