**Example 1: 查询边缘单元额外信息**



Input: 

```
tccli iecp DescribeEdgeUnitExtra --cli-unfold-argument  \
    --EdgeUnitId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c0bd6aa9-7b4f-43cd-a5e2-28ce6a1c8327",
        "APIServerType": "IP",
        "APIServerURL": "10.0.0.5",
        "APIServerURLPort": "4321",
        "APIServerResolveIP": "",
        "APIServerExposeAddress": "x.x.x.x:4321",
        "IsCreatePrometheus": false
    }
}
```

