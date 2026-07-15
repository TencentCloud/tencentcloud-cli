**Example 1: 获取车辆信息**



Input: 

```
tccli chc DescribeWorkOrderCarCollectList --cli-unfold-argument  \
    --Filters.0.Name driver-name \
    --Filters.0.Values 张
```

Output: 
```
{
    "Response": {
        "CarSet": [
            {
                "CarNumber": "京A87653",
                "DriverName": "张三",
                "DriverNumber": "******************"
            }
        ],
        "TotalCount": 2,
        "RequestId": "d842523f-f4b3-47c1-962e-04cf446241f2"
    }
}
```

