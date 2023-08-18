**Example 1: 创建VPC**



Input: 

```
tccli ecm CreateVpc --cli-unfold-argument  \
    --VpcName vpc名称 \
    --CidrBlock 10.10.0.0/28 \
    --EcmRegion ap-hangzhou-ecm \
    --Description vpc描述
```

Output: 
```
{
    "Response": {
        "RequestId": "6c7eda30-1b66-4296-857e-183f6094063f",
        "Vpc": {
            "EnableDhcp": true,
            "VpcId": "vpc-gynsaui3",
            "Description": "vpc描述",
            "DomainName": "",
            "Ipv6CidrBlock": "",
            "Region": "ap-hangzhou-ecm",
            "DhcpOptionsId": "",
            "InstanceCount": 0,
            "DnsServerSet": [],
            "EnableMulticast": false,
            "VpcName": "vpc名称",
            "AssistantCidrSet": null,
            "TagSet": null,
            "SubnetCount": 0,
            "CreatedTime": "2020-08-14 10:58:26",
            "CidrBlock": "10.10.0.0/28",
            "IsDefault": false,
            "RegionName": "杭州一区",
            "Ipv6CidrBlockSet": []
        }
    }
}
```

