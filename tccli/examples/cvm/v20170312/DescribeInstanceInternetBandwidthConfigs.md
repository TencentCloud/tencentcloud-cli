**Example 1: 查询实例带宽配置**



Input: 

```
tccli cvm DescribeInstanceInternetBandwidthConfigs --cli-unfold-argument  \
    --InstanceId ins-6lafsaz0
```

Output: 
```
{
    "Response": {
        "InternetBandwidthConfigSet": [
            {
                "StartTime": "2017-03-12T16:00:00Z",
                "EndTime": "2017-04-12T16:00:00Z",
                "InternetAccessible": {
                    "InternetMaxBandwidthOut": 50,
                    "InternetChargeType": "BANDWIDTH_PREPAID"
                }
            }
        ],
        "RequestId": "314161cd-ee40-4c37-921e-b10c4ed5607c"
    }
}
```

