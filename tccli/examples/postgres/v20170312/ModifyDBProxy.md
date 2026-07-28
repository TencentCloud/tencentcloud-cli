**Example 1: Proxy 节点变配**

变配 Proxy 节点规格与数量，下单返回 DealName

Input: 

```
tccli postgres ModifyDBProxy --cli-unfold-argument  \
    --DBInstanceId postgres-ll68q8z3 \
    --ProxyGroupId proxygroup-1x2edzxh \
    --ProxyNodeCustom.0.NodeCount 4 \
    --ProxyNodeCustom.0.Zone ap-guangzhou-3 \
    --ProxyNodeCustom.0.Cpu 4 \
    --ProxyNodeCustom.0.Mem 8 \
    --SwitchTag 0
```

Output: 
```
{
    "Response": {
        "DealName": "20260523594022883452641",
        "RequestId": "ba9bf5a6-907a-43de-b81b-41c7430c1f6c"
    }
}
```

**Example 2: 仅修改 Proxy 描述**

仅修改描述，不下单，无 DealName 返回

Input: 

```
tccli postgres ModifyDBProxy --cli-unfold-argument  \
    --DBInstanceId postgres-ll68q8z3 \
    --ProxyGroupId proxygroup-1x2edzxh \
    --Description rename proxy
```

Output: 
```
{
    "Response": {
        "RequestId": "ba9bf5a6-907a-43de-b81b-41c7430c1f6c"
    }
}
```

