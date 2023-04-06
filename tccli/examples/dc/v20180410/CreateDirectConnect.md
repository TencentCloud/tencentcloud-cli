**Example 1: 申请物理专线1**

申请物理专线，接入点为北京航信，中国移动线路，云端端口为千兆单模光口（1000Base-LX）。

Input: 

```
tccli dc CreateDirectConnect --cli-unfold-argument  \
    --DirectConnectName 北京航信物理专线1 \
    --AccessPointId ap-cn-beijing-hx \
    --LineOperator ChinaMobile \
    --CircuitCode 北京航信ANE0348NP \
    --Location 北京市海淀区西格玛A大厦14楼 \
    --PortType 1000Base-LX \
    --Bandwidth 1000 \
    --CustomerName 张三 \
    --CustomerContactMail 12345@qq.com \
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

**Example 2: 申请物理专线2**

申请物理专线，接入点为南山，中国移动线路，云端端口为千兆单模光口（1000Base-LX），有冗余专线。

Input: 

```
tccli dc CreateDirectConnect --cli-unfold-argument  \
    --DirectConnectName 物理专线1 \
    --AccessPointId ap-cn-shenzhen-ns-A \
    --LineOperator ChinaMobile \
    --CircuitCode 深圳南山ANE0348NP \
    --Location 广东省深圳市南山区科技园A大厦14楼 \
    --PortType 1000Base-LX \
    --Bandwidth 1000 \
    --RedundantDirectConnectId dc-abcdedf \
    --Vlan 100 \
    --TencentAddress 172.168.1.1/30 \
    --CustomerAddress 172.168.1.2/30 \
    --CustomerName 张三 \
    --CustomerContactMail 12345@qq.com \
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

