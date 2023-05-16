**Example 1: 查询子网下的ip使用情况，查询3个ip,只有2个ip被占用并返回资源信息**

查询子网下的ip使用情况，查询3个ip,只有2个ip被占用并返回资源信息

Input: 

```
tccli vpc DescribeUsedIpAddress --cli-unfold-argument  \
    --VpcId vpc-bx0vq623 \
    --SubnetId subnet-dl3wd0vq \
    --IpAddresses 10.0.0.1 10.0.0.2
```

Output: 
```
{
    "Response": {
        "IpAddressStates": [
            {
                "VpcId": "vpc-bx0vq623",
                "SubnetId": "subnet-dl3wd0vq",
                "IpAddress": "10.0.0.1",
                "ResourceType": "ENI",
                "ResourceId": "eni-bjekqff1"
            },
            {
                "VpcId": "vpc-bx0vq623",
                "SubnetId": "subnet-dl3wd0vq",
                "IpAddress": "10.0.0.2",
                "ResourceType": "ENI",
                "ResourceId": "eni-bjekqff2"
            }
        ],
        "TotalCount": 2,
        "RequestId": "2aaa54f5-2809-4b95-b3a5-13ce72d05759"
    }
}
```

