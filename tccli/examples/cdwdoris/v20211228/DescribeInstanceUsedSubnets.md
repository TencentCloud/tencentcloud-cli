**Example 1: 获取集群已使用子网信息**



Input: 

```
tccli cdwdoris DescribeInstanceUsedSubnets --cli-unfold-argument  \
    --InstanceId str
```

Output: 
```
{
    "Response": {
        "VpcId": "str",
        "UsedSubnets": [
            "str"
        ],
        "RequestId": "str"
    }
}
```

