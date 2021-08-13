**Example 1: 绑定防火墙实例的弹性公网ip**

仅支持新增模式的防火墙实例

Input: 

```
tccli cfw SetNatFwEip --cli-unfold-argument  \
    --OperationType bind \
    --CfwInstance cfwnat-d2afc817 \
    --EipList 1.2.3.8
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 新增防火墙实例的弹性公网ip**

仅支持新增模式的防火墙实例

Input: 

```
tccli cfw SetNatFwEip --cli-unfold-argument  \
    --OperationType newAdd \
    --CfwInstance cfwnat-d2afc817
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

