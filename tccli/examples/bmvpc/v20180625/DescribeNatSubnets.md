**Example 1: 获取NAT关联的子网信息**



Input: 

```
tccli bmvpc DescribeNatSubnets --cli-unfold-argument  \
    --NatId nat-1tw1oc0t \
    --VpcId vpc-mi51u7gs
```

Output: 
```
{
    "Response": {
        "NatSubnetInfoSet": [
            {
                "Name": "测试子网3",
                "SubnetId": "subnet-3s06hsd7",
                "SubnetNatType": 0,
                "CidrBlock": "192.168.33.0/24"
            },
            {
                "Name": "TMI",
                "SubnetId": "subnet-d3668cur",
                "SubnetNatType": 1,
                "CidrBlock": "192.168.188.0/23"
            },
            {
                "Name": "虚拟机子网1",
                "SubnetId": "subnet-hod8wpo9",
                "SubnetNatType": 1,
                "CidrBlock": "192.168.99.0/24"
            },
            {
                "Name": "H3C-测试子网1",
                "SubnetId": "subnet-kmoq5ugh",
                "SubnetNatType": 0,
                "CidrBlock": "192.168.1.0/24"
            },
            {
                "Name": "123",
                "SubnetId": "subnet-o9lo3es1",
                "SubnetNatType": 0,
                "CidrBlock": "192.168.222.0/24"
            }
        ],
        "RequestId": "b2ef2aca-f585-49fb-92cc-7889784475f5"
    }
}
```

