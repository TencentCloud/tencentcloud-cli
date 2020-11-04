**Example 1: 查询网络计费类型**

在通过api调用创建子机时，需要填写网络计费类型，通过本接口可以查询所有的网络计费类型并选择一个合适的参数。

Input: 

```
tccli cvm DescribeInternetChargeTypeConfigs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InternetChargeTypeConfigSet": [
            {
                "InternetChargeType": "BANDWIDTH_PREPAID",
                "Description": "按带宽包年包月计费"
            },
            {
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "Description": "按流量计费"
            },
            {
                "InternetChargeType": "BANDWIDTH_POSTPAID_BY_HOUR",
                "Description": "按带宽使用时长计费"
            },
            {
                "InternetChargeType": "BANDWIDTH_PACKAGE",
                "Description": "带宽包计费"
            }
        ],
        "RequestId": "c2abdac4-ea7b-4653-b07c-87cc303fabf0"
    }
}
```

