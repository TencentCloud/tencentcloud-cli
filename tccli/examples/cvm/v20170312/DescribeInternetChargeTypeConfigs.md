**Example 1: Querying the network billing methods**

When creating a CVM using API, you need to specify a network billing method. With this API, you can query the list of all network billing methods so that you can select one from them.

Input: 

```
tccli cvm DescribeInternetChargeTypeConfigs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InternetChargeTypeConfigSet": [
            {
                "InternetChargeType": "BANDWIDTH_POSTPAID_BY_MONTH",
                "Description": "Monthly postpaid"
            },
            {
                "InternetChargeType": "BANDWIDTH_PREPAID",
                "Description": "Bill by bandwidth"
            },
            {
                "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                "Description": "Bill by traffic"
            },
            {
                "InternetChargeType": "BANDWIDTH_POSTPAID_BY_HOUR",
                "Description": "Bill by bandwidth usage duration"
            },
            {
                "InternetChargeType": "BANDWIDTH_PACKAGE",
                "Description": "Bill by bandwidth package"
            }
        ],
        "RequestId": "c2abdac4-ea7b-4653-b07c-87cc303fabf0"
    }
}
```

