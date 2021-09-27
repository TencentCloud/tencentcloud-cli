**Example 1: 创建防火墙实例和接入域名**

接入模式示例

Input: 

```
tccli cfw CreateNatFwInstanceWithDomain --cli-unfold-argument  \
    --Name test \
    --Width 20 \
    --Mode 0 \
    --CrossAZone 1 \
    --NatGwList nat-14yv5rzx nat-14yv5rzk \
    --Zone ap-shanghai-4 \
    --ZoneBak ap-shanghai-3
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: CreateNatFwInstanceWithDomain**

新增模式示例

Input: 

```
tccli cfw CreateNatFwInstanceWithDomain --cli-unfold-argument  \
    --Name test \
    --Width 20 \
    --Mode 1 \
    --CrossAZone 1 \
    --NewModeItems.VpcList vpc-q98tz7hs \
    --NewModeItems.Eips 11.2.1.1 \
    --NewModeItems.AddCount 1 \
    --Zone ap-shanghai-4 \
    --ZoneBak ap-shanghai-3
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

