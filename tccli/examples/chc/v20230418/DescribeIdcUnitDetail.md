**Example 1: 查询机房管理单元信息**



Input: 

```
tccli chc DescribeIdcUnitDetail --cli-unfold-argument  \
    --IdcUnitId 2563
```

Output: 
```
{
    "Response": {
        "IdcUnitDetail": {
            "Address": "天津市滨海新区第六大街与北海路口泰达服务外包产业园信环南街9号",
            "Operator": "zhangsan",
            "TelNumber": ""
        },
        "RequestId": "545f1583-698c-4d9a-92fe-544f100769c2"
    }
}
```

