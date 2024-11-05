**Example 1: 创建防火墙实例--新增模式**

新增模式示例

Input: 

```
tccli cfw CreateNatFwInstance --cli-unfold-argument  \
    --Name NAT防火墙 \
    --Width 20 \
    --Mode 1 \
    --CrossAZone 1 \
    --NewModeItems.VpcList vpc-a1gfaf13 \
    --NewModeItems.Eips 1.1.1.1 \
    --NewModeItems.AddCount 1 \
    --Zone ap-shanghai-4 \
    --ZoneBak ap-shanghai-3
```

Output: 
```
{
    "Response": {
        "CfwInsId": "cfwnat-3c140219",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 创建NAT防火墙实例（Region参数必填）**

创建NAT防火墙实例（Region参数必填）

Input: 

```
tccli cfw CreateNatFwInstance --cli-unfold-argument  \
    --Name NAT防火墙 \
    --Width 20 \
    --Mode 0 \
    --CrossAZone 1 \
    --NatGwList nat-da1dalx nat-1dam1sd \
    --Zone ap-shanghai-4 \
    --ZoneBak ap-shanghai-3
```

Output: 
```
{
    "Response": {
        "CfwInsId": "cfwnat-12dad1ds",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

