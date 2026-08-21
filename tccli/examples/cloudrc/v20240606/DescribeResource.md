**Example 1: 资源详情**



Input: 

```
tccli cloudrc DescribeResource --cli-unfold-argument  \
    --ResourceType qcs::vpc::vpc \
    --RegionCode ap-guangzhou \
    --ResourceId vpc-m3ul053f
```

Output: 
```
{
    "Response": {
        "CreateTime": "2017-12-05 15:28:22",
        "PayMode": "Free",
        "PrivateIpAddress": [
            "10.*******"
        ],
        "Properties": "{\"CidrBlock\":\"10.*****/16\"}",
        "PublicIpAddress": [
            "139.**********"
        ],
        "RegionCode": "ap-guangzhou",
        "ResourceAlias": "******Test",
        "ResourceId": "vpc-m3ul053f",
        "ResourceType": "qcs::vpc::vpc",
        "Tags": [],
        "Uin": 909600000,
        "RequestId": "6699693a-6ef2-4707-b010-c0bb7ca83f6a"
    }
}
```

