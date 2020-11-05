**Example 1: Creating a connection**

This example shows you how to apply for a connection, where the access point is Nanshan, the ISP is China Mobile, and the Tencent Cloud port is a 1-Gigabit single-mode optical Ethernet interface (1000Base-LX), with a redundant connection.

Input: 

```
tccli dc CreateDirectConnect --cli-unfold-argument  \
    --DirectConnectName 'Connection 1'\
    --AccessPointId ap-cn-shenzhen-ns-A\
    --LineOperator ChinaMobile\
    --CircuitCode 'Shenzhen Nanshan ANE0348NP'\
    --Location '14/F, Building A, Science and Technology Park, Nanshan District, Shenzhen, Guangdong Province'\
    --PortType 1000Base-LX\
    --Bandwidth 1000\
    --RedundantDirectConnectId dc-abcdedf\
    --Vlan 100\
    --TencentAddress 172.168.1.1/30\
    --CustomerAddress 172.168.1.2/30\
    --CustomerName 'John Smith'\
    --CustomerContactMail 12345@qq.com\
    --CustomerContactNumber 18812345678
```

Output: 
```
{
    "Response": {
        "DirectConnectIdSet": [
            "dc-abcdefgh"
        ],
        "RequestId": "24a0d7e5-4c13-49be-aa16-94f698fbef3e"
    }
}
```

**Example 2: Creating a connection - 2**

This example shows you how to apply for a connection, where the access point is TravelSky, the ISP is China Mobile, and the Tencent Cloud port is a 1-Gigabit single-mode optical Ethernet interface (1000Base-LX).

Input: 

```
tccli dc CreateDirectConnect --cli-unfold-argument  \
    --DirectConnectName 'TravelSky connection 1'\
    --AccessPointId ap-cn-beijing-hx\
    --LineOperator ChinaMobile\
    --CircuitCode 'TravelSky ANE0348NP'\
    --Location '14/F, Sigma Mansion A, Haidian District, Beijing'\
    --PortType 1000Base-LX\
    --Bandwidth 1000\
    --CustomerName 'John Smith'\
    --CustomerContactMail 12345@qq.com\
    --CustomerContactNumber 18812345678
```

Output: 
```
{
    "Response": {
        "DirectConnectIdSet": [
            "dc-abcdefgh"
        ],
        "RequestId": "24a0d7e5-4c13-49be-aa16-94f698fbef3e"
    }
}
```

