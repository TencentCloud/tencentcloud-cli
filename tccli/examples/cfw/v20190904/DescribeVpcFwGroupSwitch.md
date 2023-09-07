**Example 1: VPC间防火墙开关列表**

VPC间防火墙开关列表

Input: 

```
tccli cfw DescribeVpcFwGroupSwitch --cli-unfold-argument  \
    --Filters.0.Name SwitchId \
    --Filters.0.Values cfws-18def16a8b \
    --Filters.0.OperatorType 9 \
    --Limit 10 \
    --Offset 1 \
    --StartTime 2023-03-09 20:40:19 \
    --EndTime 2023-03-09 20:40:19 \
    --Order desc \
    --By SwitchId
```

Output: 
```
{
    "Response": {
        "RequestId": "8894118f-9353-4579-8294-0582de7e3495",
        "SwitchList": [
            {
                "SwitchId": "cfwalls-1448c486f4",
                "SwitchName": "云连网 leo 测试",
                "SwitchMode": 3,
                "ConnectType": 0,
                "ConnectId": "",
                "ConnectName": "",
                "SrcInstancesInfo": [
                    {
                        "InstanceId": "vpc-dw314am3",
                        "InstanceName": "冲突sdwan",
                        "InstanceCidr": "10.24.0.0/16",
                        "Region": "ap-nanjing"
                    },
                    {
                        "InstanceId": "vpc-rkm452h0",
                        "InstanceName": "vpctest",
                        "InstanceCidr": "172.21.0.0/16,10.254.4.0/24,10.253.0.0/24",
                        "Region": "ap-beijing"
                    },
                    {
                        "InstanceId": "vpc-qdiryzpe",
                        "InstanceName": "ill-私有网络",
                        "InstanceCidr": "192.168.0.0/16",
                        "Region": "ap-shanghai"
                    }
                ],
                "DstInstancesInfo": [
                    {
                        "InstanceId": "vpc-dw314am3",
                        "InstanceName": "冲突sdwan",
                        "InstanceCidr": "10.24.0.0/16",
                        "Region": "ap-nanjing"
                    },
                    {
                        "InstanceId": "vpc-rkm452h0",
                        "InstanceName": "vpctest",
                        "InstanceCidr": "172.21.0.0/16,10.254.4.0/24,10.253.0.0/24",
                        "Region": "ap-beijing"
                    },
                    {
                        "InstanceId": "vpc-qdiryzpe",
                        "InstanceName": "ill-私有网络",
                        "InstanceCidr": "192.168.0.0/16",
                        "Region": "ap-shanghai"
                    }
                ],
                "FwGroupId": "cfwg-03508673",
                "FwGroupName": "",
                "FwInsLst": [
                    {
                        "FwInsId": "cfwew-63a110d9",
                        "FwInsName": "云连网 leo 测试-南京",
                        "FwInsRegion": "ap-nanjing"
                    }
                ],
                "Enable": 1,
                "Status": 3,
                "BypassStatus": 1,
                "AttachWithEdge": 0,
                "CrossEdgeStatus": 0,
                "IpsAction": 0
            }
        ],
        "Total": 23
    }
}
```

