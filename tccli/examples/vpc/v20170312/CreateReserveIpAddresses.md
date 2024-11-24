**Example 1: 指定个数，申请自动分配的保留 IP**

指定个数，申请自动分配的保留 IP

Input: 

```
tccli vpc CreateReserveIpAddresses --cli-unfold-argument  \
    --VpcId vpc-mcqaoy0f \
    --IpAddressCount 2 \
    --Name name_ivan \
    --Description desc_ivan
```

Output: 
```
{
    "Response": {
        "RequestId": "14c27c62-fc90-4922-a20c-fca60c6b5330",
        "ReserveIpAddressSet": [
            {
                "CreatedTime": "2024-11-21 16:57:22",
                "Description": "desc_ivan",
                "IpType": 0,
                "Name": "name_ivan",
                "ReserveIpAddress": "10.0.5.99",
                "ReserveIpId": "rsvip-eaq2f4pc",
                "ResourceId": "",
                "State": "UnBind",
                "VpcId": "vpc-mcqaoy0f"
            },
            {
                "CreatedTime": "2024-11-21 16:57:22",
                "Description": "desc_ivan",
                "IpType": 0,
                "Name": "name_ivan",
                "ReserveIpAddress": "10.0.5.50",
                "ReserveIpId": "rsvip-2g134x24",
                "ResourceId": "",
                "State": "UnBind",
                "VpcId": "vpc-mcqaoy0f"
            }
        ]
    }
}
```

