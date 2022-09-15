**Example 1: 用于获取vm的信息**



Input: 

```
tccli vpc DescribeVMInternal --cli-unfold-argument  \
    --VpcId 1 \
    --Offset 0 \
    --Limit 100 \
    --HostIp 1.1.1.1 \
    --VmIp 1.1.1.1 \
    --UniqueVpcId vpc-jmaywf6r \
    --TsvIp 1.1.1.1
```

Output: 
```
{
    "Response": {
        "Total": 9,
        "GetVmResult": [
            {
                "WanInLimit": 0,
                "VpcId": 1141,
                "VmEip": "0.0.0.0",
                "LanInLimit": 0,
                "EipType": 0,
                "VmIp": "10.0.2.10",
                "AlgFtpFlag": 0,
                "UniqueVpcId": "vpc-puh8eykn",
                "GreTunnelName": "gre1141",
                "SlaveHostIp": "1.1.1.1",
                "TsvIp": "1.1.1.1",
                "UniqueCdcId": "cdc-asdasda",
                "GroupId": [
                    0
                ],
                "CdcFlag": 0,
                "AlgSipFlag": 0,
                "EipOutLimit": 0,
                "BridgeName": "vbr1141",
                "VpcGatewayIp": "10.204.204.47",
                "Subnet": "10.0.2.0",
                "PeerIp": "0.0.0.0",
                "AliasVpcId": 0,
                "Mac": "52:54:00:12:4a:95",
                "HostIp": "10.0.2.1",
                "GatewayIp": "100.88.168.50",
                "CreateTime": "2018-08-07 06:51:35",
                "ModuleId": -1,
                "Eip": "0.0.0.0",
                "DhcpFlag": 0,
                "ForwardHostIp": "0.0.0.0",
                "LanOutLimit": 0,
                "Mask": "255.255.255.0",
                "MonitorVmFlag": 0,
                "ElasticNetworkCardName": "",
                "WanOutLimit": 0,
                "SetId": 0
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

