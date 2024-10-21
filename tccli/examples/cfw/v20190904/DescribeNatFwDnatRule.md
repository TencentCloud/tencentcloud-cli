**Example 1: 查询Nat防火墙Dnat规则示例**

查询Nat防火墙Dnat规则示例

Input: 

```
tccli cfw DescribeNatFwDnatRule --cli-unfold-argument  \
    --Limit 3 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Description": "自动化勿删",
                "FwInsId": "cfwnat-ef74fdaf",
                "Id": 6176,
                "IpProtocol": "TCP",
                "IsReferenced": 0,
                "NatGwId": "",
                "PrivateIpAddress": "10.8.1.12",
                "PrivatePort": 8080,
                "PublicIpAddress": "124.223.94.81",
                "PublicPort": 8080
            },
            {
                "Description": "自动化勿删",
                "FwInsId": "cfwnat-ef74fdaf",
                "Id": 6175,
                "IpProtocol": "TCP",
                "IsReferenced": 0,
                "NatGwId": "",
                "PrivateIpAddress": "10.8.2.4",
                "PrivatePort": 80,
                "PublicIpAddress": "124.223.94.81",
                "PublicPort": 80
            },
            {
                "Description": "test",
                "FwInsId": "cfwnat-dce8698e",
                "Id": 6126,
                "IpProtocol": "UDP",
                "IsReferenced": 0,
                "NatGwId": "",
                "PrivateIpAddress": "172.16.0.17",
                "PrivatePort": 65530,
                "PublicIpAddress": "43.138.154.20",
                "PublicPort": 65530
            }
        ],
        "RequestId": "d6ab3ac9-0902-48f3-8753-c0a48adcfc3f",
        "Total": 5
    }
}
```

