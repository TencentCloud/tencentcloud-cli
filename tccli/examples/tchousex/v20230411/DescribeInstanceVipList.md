**Example 1: DescribeInstanceVipList**

获取集群的vip相关列表信息

Input: 

```
tccli tchousex DescribeInstanceVipList --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "InstanceID": "abc",
        "InstanceName": "abc",
        "Region": "abc",
        "RegionDesc": "abc",
        "VpcId": "abc",
        "SubnetId": "abc",
        "VipInfoList": [
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

