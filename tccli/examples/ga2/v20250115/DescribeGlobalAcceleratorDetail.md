**Example 1: 测试用例**



Input: 

```
tccli ga2 DescribeGlobalAcceleratorDetail --cli-unfold-argument  \
    --GlobalAcceleratorIds ga-fkp1vr85
```

Output: 
```
{
    "Response": {
        "AcceleratorSet": [
            {
                "AcceleratorAreaCounts": 0,
                "AppId": "1255486055",
                "Cname": "ga-cxwyu5cn-pre.tencentcloudga010.cn",
                "CreateTime": "2025-12-19 15:10:17",
                "CrossBorderStatus": "false",
                "Description": "",
                "GaWanId": "",
                "GlobalAcceleratorId": "ga-cxwyu5cn",
                "InstanceChargeType": "POSTPAID",
                "ListenerCounts": 2,
                "Name": "garendu-tesst-trade",
                "OwnerUin": "100002840660",
                "Status": "active",
                "UpdateTime": "2025-12-22 11:45:22"
            }
        ],
        "TotalCount": 3,
        "RequestId": "3ecda282-bb4b-473b-beed-456298d8d076"
    }
}
```

