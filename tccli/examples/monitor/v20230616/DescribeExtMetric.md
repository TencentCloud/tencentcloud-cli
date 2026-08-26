**Example 1: 查询对外指标**



Input: 

```
tccli monitor DescribeExtMetric --cli-unfold-argument  \
    --ExtNamespace QCE/LB
```

Output: 
```
{
    "Response": {
        "ExtMetricList": [
            {
                "CNMeaning": "连接数量",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "VConnum",
                "Unit": "count"
            },
            {
                "CNMeaning": "新建连接",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "VNewConn",
                "Unit": "count"
            },
            {
                "CNMeaning": "入包量",
                "EnMeaning": "Inpkg",
                "MetricCName": "入包量",
                "MetricName": "VInpkg",
                "Unit": "count"
            },
            {
                "CNMeaning": "入带宽",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "VIntraffic",
                "Unit": "bps"
            },
            {
                "CNMeaning": "出包量",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "VOutpkg",
                "Unit": "count/s"
            },
            {
                "CNMeaning": "出带宽",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "VOuttraffic",
                "Unit": "bps"
            },
            {
                "CNMeaning": "出带宽",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "TotalOuttraffic",
                "Unit": "Mbps"
            },
            {
                "CNMeaning": "出包量",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "PvvOutpkg",
                "Unit": "count"
            },
            {
                "CNMeaning": "入包量",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "PvvInpkg",
                "Unit": "count"
            },
            {
                "CNMeaning": "出带宽",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "PvvOuttraffic",
                "Unit": "bps"
            },
            {
                "CNMeaning": "入带宽",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "PvvIntraffic",
                "Unit": "bps"
            },
            {
                "CNMeaning": "连接数量",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "PvvConnum",
                "Unit": "count"
            },
            {
                "CNMeaning": "不活跃连接",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "PvvInactiveConn",
                "Unit": "count"
            },
            {
                "CNMeaning": "新建连接",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "PvvNewConn",
                "Unit": "count"
            },
            {
                "CNMeaning": "出包量",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "RvOutpkg",
                "Unit": "count"
            },
            {
                "CNMeaning": "入包量",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "RvInpkg",
                "Unit": "count"
            },
            {
                "CNMeaning": "出带宽",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "RvOuttraffic",
                "Unit": "bps"
            },
            {
                "CNMeaning": "入流量",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "RvIntraffic",
                "Unit": "bps"
            },
            {
                "CNMeaning": "连接数量",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "RvConnum",
                "Unit": "count"
            },
            {
                "CNMeaning": "不活跃连接",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "RvInactiveConn",
                "Unit": "count"
            },
            {
                "CNMeaning": "新建连接",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "RvNewConn",
                "Unit": "count"
            },
            {
                "CNMeaning": "外网入包量",
                "EnMeaning": "VipInpkg",
                "MetricCName": "外网入包量",
                "MetricName": "VipInpkg",
                "Unit": "count/s"
            },
            {
                "CNMeaning": "外网入带宽",
                "EnMeaning": "VipIntraffic",
                "MetricCName": "外网入带宽",
                "MetricName": "VipIntraffic",
                "Unit": "Mbps"
            },
            {
                "CNMeaning": "外网出包量",
                "EnMeaning": "VipOutpkg",
                "MetricCName": "外网出包量",
                "MetricName": "VipOutpkg",
                "Unit": "count/s"
            },
            {
                "CNMeaning": "外网出带宽",
                "EnMeaning": "VipOuttraffic",
                "MetricCName": "外网出带宽",
                "MetricName": "VipOuttraffic",
                "Unit": "Mbps"
            },
            {
                "CNMeaning": "外网出流量",
                "EnMeaning": "",
                "MetricCName": "",
                "MetricName": "AccOuttraffic",
                "Unit": "MB"
            },
            {
                "CNMeaning": "公网入带宽利用率",
                "EnMeaning": "vip_in_traffic_ratio",
                "MetricCName": "公网入带宽利用率",
                "MetricName": "IntrafficVipRatio",
                "Unit": "%"
            },
            {
                "CNMeaning": "公网出带宽利用率",
                "EnMeaning": "vip_out_traffic_ratio",
                "MetricCName": "公网出带宽利用率",
                "MetricName": "OuttrafficVipRatio",
                "Unit": "%"
            },
            {
                "CNMeaning": "丢弃的入向包量",
                "EnMeaning": "Dropped packets in",
                "MetricCName": "外网入向丢包量",
                "MetricName": "Vipindroppkts",
                "Unit": "pps"
            },
            {
                "CNMeaning": "丢弃的出向包量",
                "EnMeaning": "Dropped packets out",
                "MetricCName": "外网出向丢包量",
                "MetricName": "Vipoutdroppkts",
                "Unit": "pps"
            }
        ],
        "RequestId": "f64026ab-1153-411e-859b-c2b2ad64ab41"
    }
}
```

