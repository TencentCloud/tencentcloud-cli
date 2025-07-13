**Example 1: 获取风险调用记录列表**



Input: 

```
tccli csip DescribeRiskCallRecord --cli-unfold-argument  \
    --RiskID 10091
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CallCount": 0,
                "EventDescCN": "卸载主机安全客户端",
                "EventDescEN": "DeleteMachine",
                "EventName": "DeleteMachine",
                "ProductName": "cwp",
                "ProductNameCN": "主机安全"
            }
        ],
        "RequestId": "728a0b3b-230d-468e-a10a-f6e7a56c0056",
        "Total": 1
    }
}
```

