**Example 1: 查询网关API监控明细数据**



Input: 

```
tccli tsf DescribeApiUseDetail --cli-unfold-argument  \
    --ApiId api-qabo8xyl \
    --GatewayDeployGroupId group-i54lzdrq \
    --EndTime '2020-09-22 00:00:00' \
    --StartTime '2020-09-22 00:00:00'
```

Output: 
```
{
    "Response": {
        "Result": {
            "TopStatusCode": [
                {
                    "Count": "2000",
                    "Ratio": "0.35565",
                    "Name": "2xx"
                }
            ],
            "TopTimeCost": [
                {
                    "Count": "xx",
                    "Ratio": "xx",
                    "Name": "xx"
                }
            ],
            "Quantile": {
                "NinthPositionValue": "12.13",
                "MinValue": "0.32",
                "MaxValue": "0.26",
                "FifthPositionValue": "1.32"
            }
        },
        "RequestId": "5d996e05507e42d5970cd2e25ed5267a"
    }
}
```

