**Example 1: 创建新增模式的防火墙实例**

新增模式示例

Input: 

```
tccli cfw CreateNatFwInstanceWithDomain --cli-unfold-argument  \
    --Name NAT防火墙 \
    --Width 20 \
    --Mode 1 \
    --CrossAZone 1 \
    --NewModeItems.VpcList vpc-38s9y0w1 \
    --NewModeItems.Eips 1.1.1.1 \
    --NewModeItems.AddCount 1 \
    --Zone ap-shanghai-4 \
    --ZoneBak ap-shanghai-3
```

Output: 
```
{
    "Response": {
        "CfwInsId": "cfwnat-f0f1c7c0",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 创建防火墙实例和接入域名**

接入模式示例

Input: 

```
tccli cfw CreateNatFwInstanceWithDomain --cli-unfold-argument  \
    --Name NAT防火墙 \
    --Width 20 \
    --Mode 0 \
    --CrossAZone 1 \
    --NatGwList nat-m6otefcc nat-m6otefcd \
    --Zone ap-shanghai-4 \
    --ZoneBak ap-shanghai-3
```

Output: 
```
{
    "Response": {
        "CfwInsId": "cfwnat-f0f1c7c0",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

