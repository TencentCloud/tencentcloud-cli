**Example 1: 修改物理专线属性信息**



Input: 

```
tccli dc ModifyDirectConnectAttribute --cli-unfold-argument  \
    --DirectConnectId dcx-abcdefgh \
    --DirectConnectName abc \
    --CircuitCode ABF_123 \
    --Vlan 100 \
    --TencentAddress 172.168.1.1/30 \
    --CustomerAddress 172.168.1.2/30 \
    --CustomerName 张三 \
    --CustomerContactMail 12345@qq.com \
    --CustomerContactNumber 18812345678 \
    --Bandwidth 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

