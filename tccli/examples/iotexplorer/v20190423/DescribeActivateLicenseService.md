**Example 1: 实例详情**



Input: 

```
tccli iotexplorer DescribeActivateLicenseService --cli-unfold-argument  \
    --InstanceId ins-BoSq3gRJ27
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "LicenseType": "TWeCall",
                "TotalNum": 4000,
                "UsedNum": 0,
                "TWeCallLicense": [
                    {
                        "TWeCallType": "TWeCall_A",
                        "TotalNum": 1000,
                        "UsedNum": 0
                    }
                ]
            }
        ],
        "RequestId": "00a70e11-d755-40f8-8f55-e951d7d30036"
    }
}
```

