**Example 1: 防火墙垂直扩容**



Input: 

```
tccli cfw ExpandCfwVertical --cli-unfold-argument  \
    --FwType nat \
    --Width 200 \
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

**Example 2: 防火墙规格调整开启弹性计费**



Input: 

```
tccli cfw ExpandCfwVertical --cli-unfold-argument  \
    --FwType nat \
    --Width 200 \
    --CfwInstance cfwnat-d2afc817 \
    --ElasticSwitch 1 \
    --ElasticBandwidth 220
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

