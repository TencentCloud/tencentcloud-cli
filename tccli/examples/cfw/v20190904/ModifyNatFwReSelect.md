**Example 1: 接入模式防火墙实例重新选择接入nat**

接入模式示例

Input: 

```
tccli cfw ModifyNatFwReSelect --cli-unfold-argument  \
    --Mode 1 \
    --CfwInstance cfwnat-d2afc817 \
    --NatGwList nat-14yv5rzx nat-14yv5rzk
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 新增模式防火墙实例重新选择接入vpc**

新增模式示例

Input: 

```
tccli cfw ModifyNatFwReSelect --cli-unfold-argument  \
    --Mode 0 \
    --CfwInstance cfwnat-d2afc817 \
    --VpcList vpc-q98tz7hs vpc-x98tz7ha
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

