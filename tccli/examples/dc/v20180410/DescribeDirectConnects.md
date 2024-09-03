**Example 1: 查询物理专线列表-1**

使用Filter进行筛选，用direct-connect-name进行筛选。

Input: 

```
tccli dc DescribeDirectConnects --cli-unfold-argument  \
    --Filters.0.Name direct-connect-name \
    --Filters.0.Values 专线接入
```

Output: 
```
{
    "Response": {
        "DirectConnectSet": [
            {
                "DirectConnectId": "dc-c3hbbsw9",
                "DirectConnectName": "专线接入测试",
                "RedundantDirectConnectId": "",
                "State": "AVAILABLE",
                "ChargeState": "NORMAL",
                "AccessPointId": "ap-cn-guangzhou-kxc",
                "AccessPointName": "广州科丰路",
                "AccessPointType": "VXLAN",
                "Bandwidth": 10000,
                "LineOperator": "ChinaOther",
                "Construct": 1,
                "Location": "广东省广州市华新园0602-A01机架7号位",
                "PortType": "10GBase-LR",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "StartTime": "2019-09-12 17:09:07",
                "CircuitCode": "唐镇0103-A09-PL01-1",
                "Vlan": 100,
                "CustomerName": "张三",
                "CustomerContactMail": "zhangsan@tencent.com",
                "CustomerContactNumber": "13888888888",
                "FaultReportContactPerson": "李四",
                "FaultReportContactNumber": "15999999999",
                "IdcCity": "广东省广州市华新园0602-A01机架7号位",
                "SignLaw": false,
                "LocalZone": false,
                "VlanZeroDirectConnectTunnelCount": 0,
                "OtherVlanDirectConnectTunnelCount": 0,
                "MinBandwidth": 0,
                "ExpiredTime": null,
                "EnabledTime": "2020-09-22T00:00:00+00:00",
                "TencentAddress": "192.168.1.2/24",
                "CustomerAddress": "192.168.1.1/24",
                "ChargeType": "NON_RECURRING_CHARGE",
                "TagSet": []
            }
        ],
        "RequestId": "edafc0e0-3a01-4ac3-848d-e402ff04c1f3",
        "TotalCount": 1,
        "AllSignLaw": false
    }
}
```

**Example 2: 查询物理专线列表-2**

指定DirectConnectIds查询物理专线列表。

Input: 

```
tccli dc DescribeDirectConnects --cli-unfold-argument  \
    --DirectConnectIds dc-c3hbbsw9
```

Output: 
```
{
    "Response": {
        "DirectConnectSet": [
            {
                "DirectConnectId": "dc-c3hbbsw9",
                "DirectConnectName": "专线接入测试",
                "RedundantDirectConnectId": "",
                "State": "AVAILABLE",
                "ChargeState": "NORMAL",
                "AccessPointId": "ap-cn-guangzhou-kxc",
                "AccessPointName": "广州科丰路",
                "AccessPointType": "VXLAN",
                "Bandwidth": 10000,
                "LineOperator": "ChinaOther",
                "Construct": 1,
                "Location": "广东省广州市华新园0602-A01机架7号位",
                "PortType": "10GBase-LR",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "StartTime": "2019-09-12 17:09:07",
                "CircuitCode": "唐镇0103-A09-PL01-1",
                "Vlan": 100,
                "CustomerName": "张三",
                "CustomerContactMail": "zhangsan@tencent.com",
                "CustomerContactNumber": "13888888888",
                "FaultReportContactPerson": "李四",
                "FaultReportContactNumber": "15999999999",
                "IdcCity": "广东省广州市华新园0602-A01机架7号位",
                "SignLaw": false,
                "LocalZone": false,
                "VlanZeroDirectConnectTunnelCount": 0,
                "OtherVlanDirectConnectTunnelCount": 0,
                "MinBandwidth": 0,
                "ExpiredTime": null,
                "EnabledTime": "2020-09-22T00:00:00+00:00",
                "TencentAddress": "192.168.1.2/24",
                "CustomerAddress": "192.168.1.1/24",
                "ChargeType": "NON_RECURRING_CHARGE",
                "TagSet": []
            }
        ],
        "RequestId": "edafc0e0-3a01-4ac3-848d-e402ff04c1f3",
        "TotalCount": 1,
        "AllSignLaw": false
    }
}
```

