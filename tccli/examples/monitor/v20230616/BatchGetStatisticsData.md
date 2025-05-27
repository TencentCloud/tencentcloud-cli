**Example 1: 获取带宽Top5数据**



Input: 

```
tccli monitor BatchGetStatisticsData --cli-unfold-argument  \
    --Period 60 \
    --ViewName lb_appid_netgroup_u_id \
    --MetricName outtraffic \
    --Namespace qce/lb \
    --StartTime 2024-12-13T12:07:32+08:00 \
    --EndTime 2024-12-13T12:37:32+08:00 \
    --Statistics avg \
    --Expr.Function TOP \
    --Expr.N 5 \
    --DimensionsList.0.Dimensions.0.Name netgroup \
    --DimensionsList.0.Dimensions.0.Value bwp-djhptxvq \
    --DimensionsList.0.Dimensions.1.Name u_id \
    --DimensionsList.0.Dimensions.1.Value eip-9i8lgqjq \
    --DimensionsList.0.Dimensions.2.Name appid \
    --DimensionsList.0.Dimensions.2.Value 1251001034
```

Output: 
```
{
    "Response": {
        "RequestId": "58fa6216-f381-49a5-9a5f-cd52f57fdd85",
        "Msg": "Success",
        "StartTime": "2024-12-13T12:07:00+08:00",
        "EndTime": "2024-12-13T12:37:59+08:00",
        "Period": 60,
        "MetricName": "outtraffic",
        "DataPoints": [
            {
                "Dimensions": [
                    {
                        "Name": "netgroup",
                        "Value": "bwp-djhptxvq"
                    },
                    {
                        "Name": "u_id",
                        "Value": "eip-9i8lgqjq"
                    },
                    {
                        "Name": "appid",
                        "Value": "1251001034"
                    }
                ],
                "Timestamps": [
                    1734064020,
                    1734063360,
                    1734063960,
                    1734063000,
                    1734063540
                ],
                "Values": [
                    43332685.733330004,
                    31184567.066670004,
                    13895291.06667,
                    11419580.8,
                    10010704.13333
                ]
            }
        ]
    }
}
```

