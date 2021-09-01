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
        "RequestId": "xx",
        "Data": [
            {
                "Key": "xx",
                "Value": 21,
                "Label": "xx",
                "TimeStamp": "312312"
            }
        ]
    }
}
```

