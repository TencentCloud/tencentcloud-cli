**Example 1: 查询CCN关联的实例信息（返回结果排除掉了云防火墙在CCN中创建的引流网络实例）**



Input: 

```
tccli cfw DescribeCcnAssociatedInstances --cli-unfold-argument  \
    --CcnId ccn-iidlg5oh
```

Output: 
```
{
    "Response": {
        "CcnAssociatedInstances": [
            {
                "CidrLst": [
                    "172.16.0.0/20"
                ],
                "InsType": "VPC",
                "InstanceId": "vpc-o7irzxwt",
                "InstanceName": "gwlb-dpdk-u6cd5u5170u514bu798f",
                "InstanceRegion": "eu-frankfurt"
            }
        ],
        "Total": 3,
        "RequestId": "de54f1ed-5a43-47e7-b57b-4892526e4cf7"
    }
}
```

