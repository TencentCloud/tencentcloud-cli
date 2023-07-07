**Example 1: 查询VPC列表**

查询VPC列表

Input: 

```
tccli ecm DescribeVpcs --cli-unfold-argument  \
    --VpcIds vpc-07kqm4uj \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "d15a17b7-703b-4757-ae1a-745af315abc4",
        "VpcSet": [
            {
                "EnableDhcp": true,
                "Ipv6ISP": "CMCC",
                "VpcId": "vpc-07kqm4uj",
                "Ipv6CidrBlockSet": [
                    {
                        "IPv6CidrBlock": "240e:95a:3002:1e::/64",
                        "ISPType": "CTCC"
                    }
                ],
                "Description": "",
                "DomainName": "",
                "Ipv6CidrBlock": "",
                "Region": "ap-hangzhou-ecm",
                "DhcpOptionsId": "",
                "InstanceCount": 2,
                "DnsServerSet": [],
                "EnableMulticast": false,
                "VpcName": "Default-VPC",
                "AssistantCidrSet": [],
                "TagSet": null,
                "SubnetCount": 1,
                "CreatedTime": "2020-06-17 12:09:46",
                "CidrBlock": "172.16.0.0/16",
                "IsDefault": true,
                "RegionName": "杭州一区"
            }
        ]
    }
}
```

