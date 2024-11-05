**Example 1: 专家服务-可用订单详情**

专家服务-可用订单详情

Input: 

```
tccli cwp DescribeAvailableExpertServiceDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "48ca3c70-801e-48b1-80a7-1007afbf5ffb",
        "EmergencyResponse": 7,
        "ExpertService": [
            {
                "OrderId": 10021,
                "InquireType": 2,
                "InquireNum": 1022,
                "BeginTime": "2024-11-04 21:24:47",
                "EndTime": "2024-11-04 21:24:55",
                "ServiceTime": 134952943,
                "Status": 2
            }
        ],
        "ProtectNet": 2,
        "ExpertServiceBuy": true,
        "EmergencyResponseBuy": true,
        "ProtectNetBuy": true
    }
}
```

