**Example 1: 创建VPC**



Input: 

```
tccli vpc CreateVpc --cli-unfold-argument  \
    --VpcName TestVPC \
    --CidrBlock 10.8.0.0/16 \
    --Tags.0.Value shanghai \
    --Tags.0.Key city
```

Output: 
```
{
    "Response": {
        "Vpc": {
            "VpcId": "vpc-4tboefn3",
            "VpcName": "TestVPC",
            "CidrBlock": "10.8.0.0/16",
            "Ipv6CidrBlock": "",
            "IsDefault": false,
            "EnableMulticast": false,
            "CreatedTime": "2020-09-24 15:57:39",
            "EnableDhcp": true,
            "DhcpOptionsId": "dopt-5f5lzouo",
            "DnsServerSet": [
                "183.60.82.98",
                "183.60.83.1"
            ],
            "DomainName": "",
            "TagSet": [],
            "AssistantCidrSet": [
                {
                    "CidrBlock": "172.16.0.0/16",
                    "AssistantType": 0,
                    "SubnetSet": []
                }
            ]
        },
        "RequestId": "680f4013-31a3-440a-bc09-fd9348a90900"
    }
}
```

