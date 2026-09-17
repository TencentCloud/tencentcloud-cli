**Example 1: 查询对端网关**

查询对端网关

Input: 

```
tccli vpc DescribeCustomerGateways --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CustomerGatewaySet": [
            {
                "BgpAsn": 0,
                "CreatedTime": "2026-07-06 23:00:09",
                "CustomerGatewayId": "cgw-dby2ybob",
                "CustomerGatewayName": "cgw-01",
                "IpAddress": "43.1****0.53",
                "TagSet": [],
                "VpnConnNum": 2
            }
        ],
        "TotalCount": 1,
        "RequestId": "4ec28434-c40f-450d-a58e-7b001bcb4d58"
    }
}
```

