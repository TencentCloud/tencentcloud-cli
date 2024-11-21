**Example 1: 查看对象列表**



Input: 

```
tccli waf DescribeObjects --cli-unfold-argument  \
    --Filters.0.Name Status \
    --Filters.0.Values 1 \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "ClbObjects": [
            {
                "ApiStatus": 0,
                "BotStatus": 0,
                "ClsStatus": 0,
                "InstanceId": "waf_2kuil2ft02vqm7z3",
                "InstanceLevel": 3,
                "InstanceName": "gz-Default1",
                "IpHeaders": [
                    "spheader",
                    "myheader"
                ],
                "NumericalVpcId": -1,
                "ObjectFlowMode": 1,
                "ObjectId": "lb-70mdt3it",
                "ObjectName": "zunhua-multi-test_pjk1",
                "PostCKafkaStatus": 0,
                "PostCLSStatus": 0,
                "PreciseDomains": [],
                "PrivateIp": [
                    "121.123.11.7"
                ],
                "Proxy": 3,
                "PublicIp": [
                    "139.186.100.71"
                ],
                "Region": "ap-chongqing",
                "Status": 1,
                "Type": "CLB",
                "VirtualDomain": "lb-70mdt3it.clb-default.qcloudwaf.com",
                "Vpc": "vpc-jl1cw1e9",
                "VpcName": "Default-VPC"
            }
        ],
        "RequestId": "6ceb784e-b440-4cac-81ee-0b87ffe81e6f"
    }
}
```

