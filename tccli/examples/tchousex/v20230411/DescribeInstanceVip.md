**Example 1: DescribeInstanceVip**

获取集群的vip相关信息

Input: 

```
tccli tchousex DescribeInstanceVip --cli-unfold-argument  \
    --InstanceId abc \
    --Cluster abc
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "VipInfo": [
            {
                "InstanceId": "abc",
                "VirtualCluster": "abc",
                "ResourceId": "abc",
                "Status": 0,
                "Vip": "abc",
                "Port": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

