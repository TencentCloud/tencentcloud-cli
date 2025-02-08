**Example 1: 获取服务内网Vip信息**

获取服务内网Vip信息

Input: 

```
tccli tccatalog DescribeTccVipInternal --cli-unfold-argument  \
    --CatalogId b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1
```

Output: 
```
{
    "Response": {
        "TccVipInternalSet": [
            {
                "Type": "HIVE",
                "Vip": "127.0.0.1",
                "Vport": 7004
            }
        ],
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

