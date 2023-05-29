**Example 1: 获取流量趋势数据**



Input: 

```
tccli waf DescribeFlowTrend --cli-unfold-argument  \
    --Domain www.baidu.com \
    --StartTs 1620144000 \
    --EndTs 1620180000
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Data": [
            {
                "Key": "/api/cf/v4/user/get-info",
                "Value": 21,
                "Label": "/api/cf/v4/user/get-info",
                "TimeStamp": "2021-04-22 20:30:00"
            }
        ]
    }
}
```

