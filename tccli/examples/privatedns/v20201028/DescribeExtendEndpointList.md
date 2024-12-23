**Example 1: 获取出站终端节点列表**

获取出站终端节点列表

Input: 

```
tccli privatedns DescribeExtendEndpointList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "3a0ce2a9-d277-4fb9-9f58-93f78aa375c1",
        "TotalCount": 4,
        "OutboundEndpointSet": [
            {
                "EndpointId": "eid-xxxxxxxx",
                "EndpointName": "测试终端节点",
                "Region": "ap-guangzhou",
                "Tags": [],
                "EndpointServiceSet": [
                    {
                        "AccessType": "CLB",
                        "Vip": "11.158.31.145",
                        "Vport": "10118",
                        "Pip": "10.110.2.8",
                        "Pport": "53",
                        "Proto": "udp",
                        "VpcId": "vpc-xxxxxxx",
                        "Region": "ap-guangzhou",
                        "SnatVipCidr": "11.163.0.0/16"
                    }
                ]
            },
            {
                "EndpointId": "eid-xxxxxxxx",
                "EndpointName": "测试终端节点",
                "Region": "ap-guangzhou",
                "Tags": [],
                "EndpointServiceSet": [
                    {
                        "AccessType": "CLB",
                        "Vip": "11.158.31.145",
                        "Vport": "10118",
                        "Pip": "10.110.2.8",
                        "Pport": "53",
                        "Proto": "udp",
                        "VpcId": "vpc-xxxxxxx",
                        "Region": "ap-guangzhou",
                        "SnatVipCidr": "11.163.0.0/16"
                    }
                ]
            },
            {
                "EndpointId": "eid-6cb19fe2b6",
                "EndpointName": "测试终端节点",
                "Region": "ap-guangzhou",
                "Tags": [],
                "EndpointServiceSet": [
                    {
                        "AccessType": "CCN",
                        "Vip": "11.158.31.145",
                        "Vport": "10493",
                        "Pip": "10.111.111.111",
                        "Pport": "53",
                        "Proto": "udp",
                        "VpcId": "vpc-xxxxxxx",
                        "Region": "ap-guangzhou",
                        "SnatVipSet": "10.110.1.4;10.110.1.13"
                    }
                ]
            },
            {
                "EndpointId": "eid-xxxxxxx",
                "EndpointName": "测试终端节点",
                "Region": "ap-guangzhou",
                "Tags": [],
                "EndpointServiceSet": [
                    {
                        "AccessType": "CLB",
                        "Vip": "11.158.31.145",
                        "Vport": "10118",
                        "Pip": "10.110.2.8",
                        "Pport": "53",
                        "Proto": "udp",
                        "VpcId": "vpc-xxxxxxx",
                        "Region": "ap-xxxxxxxx",
                        "SnatVipCidr": "11.163.0.0/16"
                    }
                ]
            }
        ]
    }
}
```

