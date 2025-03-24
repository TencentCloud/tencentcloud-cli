**Example 1: 查询机房管理单元信息**



Input: 

```
tccli chc DescribeIdcUnitAssetDetail --cli-unfold-argument  \
    --IdcUnitId 2569
```

Output: 
```
{
    "Response": {
        "IdcUnitDetail": {
            "Address": "天津市滨海新区第六大街与北海路口泰达服务外包产业园信环南街",
            "AssetManager": "张三",
            "AssetManagerTelNumber": "1380013800",
            "Operator": "zhangsan",
            "TelNumber": ""
        },
        "RequestId": "8616a5eb-6edd-4d76-b081-fc4c429c3162"
    }
}
```

