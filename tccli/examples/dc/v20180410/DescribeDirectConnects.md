**Example 1: 查询物理专线列表**

使用Filter进行筛选，用direct-connect-name进行筛选；

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
                "EnabledTime": "2018-06-02 15:12:34",
                "CustomerContactNumber": "18812345678",
                "AccessPointId": "ap-cn-shenzhen-ns-A",
                "ChargeState": "NORMAL",
                "DirectConnectId": "dc-gd3u0zov",
                "State": "AVAILABLE",
                "ExpiredTime": null,
                "Location": "深南大道万利达大厦13楼591",
                "CreatedTime": "2018-05-03 15:12:34",
                "PortType": "1000Base-T",
                "CustomerName": "张三",
                "LineOperator": "ChinaTelecom",
                "TencentAddress": "192.168.1.2/30",
                "CircuitCode": "",
                "CustomerAddress": "192.168.1.1/30",
                "CustomerContactMail": "zzuzxy1111@163.com",
                "Vlan": 10,
                "Bandwidth": 100,
                "DirectConnectName": "用户自建专线接入",
                "ChargeType": "NON_RECURRING_CHARGE",
                "RedundantDirectConnectId": ""
            },
            {
                "EnabledTime": "2018-05-23 11:10:46",
                "CustomerContactNumber": "18812345678",
                "AccessPointId": "ap-cn-beijing-hx",
                "ChargeState": "NORMAL",
                "DirectConnectId": "dc-2zeyish1",
                "State": "BUILDING",
                "ExpiredTime": null,
                "Location": "西土城路10号北京邮电大学",
                "CreatedTime": "2018-04-23 11:10:46",
                "PortType": "1000Base-T",
                "CustomerName": "张三",
                "LineOperator": "ChinaMobile",
                "TencentAddress": "192.168.1.156/24",
                "CircuitCode": "",
                "CustomerAddress": "192.168.1.157/24",
                "CustomerContactMail": "zzuzxy@163.com",
                "Vlan": 253,
                "Bandwidth": 2,
                "DirectConnectName": "专线接入一次性付费测试",
                "ChargeType": "PREPAID_BY_YEAR",
                "RedundantDirectConnectId": ""
            },
            {
                "EnabledTime": "2018-05-23 10:28:12",
                "CustomerContactNumber": "18812345678",
                "AccessPointId": "ap-cn-shenzhen-ns-A",
                "ChargeState": "NORMAL",
                "DirectConnectId": "dc-epeq2tj7",
                "State": "BUILDING",
                "ExpiredTime": null,
                "Location": "万利达大厦13楼591房间",
                "CreatedTime": "2018-04-23 10:28:12",
                "PortType": "1000Base-T",
                "CustomerName": "张三",
                "LineOperator": "ChinaMobile",
                "TencentAddress": "192.168.1.2/30",
                "CircuitCode": "",
                "CustomerAddress": "192.168.1.1/30",
                "CustomerContactMail": "zzuzxy@163.com",
                "Vlan": 100,
                "Bandwidth": 2,
                "DirectConnectName": "专线接入一次性付费测试",
                "ChargeType": "NON_RECURRING_CHARGE",
                "RedundantDirectConnectId": ""
            }
        ],
        "RequestId": "70d690c8-477a-4e5d-99c0-fa1bb012a105",
        "TotalCount": 3
    }
}
```

**Example 2: 查询物理专线列表-2**



Input: 

```
tccli dc DescribeDirectConnects --cli-unfold-argument  \
    --DirectConnectIds dc-6mqd6t9j
```

Output: 
```
{
    "Response": {
        "DirectConnectSet": [
            {
                "EnabledTime": "2019-03-30 09:48:39",
                "CustomerContactNumber": "13924777788",
                "AccessPointId": "ap-cn-shenzhen-ns-A",
                "ChargeState": "NORMAL",
                "DirectConnectId": "dc-6mqd6t9j",
                "State": "PENDING",
                "ExpiredTime": null,
                "Location": "腾讯大厦",
                "CreatedTime": "2019-02-28 09:48:39",
                "PortType": "1000Base-LX",
                "CustomerName": "张三",
                "LineOperator": "ChinaTelecom",
                "TencentAddress": "",
                "CircuitCode": "",
                "CustomerAddress": "",
                "CustomerContactMail": "zzubupt@163.com",
                "Vlan": -1,
                "Bandwidth": 100,
                "DirectConnectName": "bbb",
                "ChargeType": "PREPAID_BY_YEAR",
                "RedundantDirectConnectId": ""
            }
        ],
        "RequestId": "a17e965b-5c58-4cf2-b5fb-2e00946deea8",
        "TotalCount": 1
    }
}
```

