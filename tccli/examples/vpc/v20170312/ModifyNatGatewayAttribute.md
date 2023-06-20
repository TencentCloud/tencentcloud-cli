**Example 1: 修改NAT网关的属性**

只支持修改NAT网关的名称和NAT网关最大外网出带宽。更新NAT网关并发连接上限请使用ResetNatGatewayConnection接口。

Input: 

```
tccli vpc ModifyNatGatewayAttribute --cli-unfold-argument  \
    --InternetMaxBandwidthOut 500 \
    --NatGatewayId nat-ig8xpno8 \
    --NatGatewayName 测试nat网关
```

Output: 
```
{
    "Response": {
        "RequestId": "e5c289dc-bf4b-4828-8093-3c434d1f0886"
    }
}
```

**Example 2: 变更NAT实例的SNAT模式**

修改NAT网关的StrictSnatMode开关

Input: 

```
tccli vpc ModifyNatGatewayAttribute --cli-unfold-argument  \
    --NatGatewayId nat-owj32fec
```

Output: 
```
{
    "Response": {
        "RequestId": "5acefde4-3be5-4582-a432-742081e1c904"
    }
}
```

