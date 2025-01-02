**Example 1: 获取账户信息**



Input: 

```
tccli scf GetAccount --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AccountUsage": {
            "NamespacesCount": 1,
            "Namespace": [
                {
                    "Namespace": "default",
                    "Functions": [
                        "express_demo-test"
                    ],
                    "TotalConcurrencyMem": 0,
                    "TotalAllocatedConcurrencyMem": 0,
                    "TotalAllocatedProvisionedMem": 0,
                    "FunctionsCount": 1
                }
            ],
            "TotalConcurrencyMem": 128000,
            "TotalAllocatedConcurrencyMem": 0,
            "UserConcurrencyMemLimit": 128000
        },
        "AccountLimit": {
            "NamespacesCount": 5,
            "Namespace": [
                {
                    "Namespace": "default",
                    "FunctionsCount": 50,
                    "TimeoutLimit": 900,
                    "InitTimeoutLimit": 300,
                    "TestModelLimit": 20,
                    "RetryNumLimit": 2,
                    "MinMsgTTL": 60,
                    "MaxMsgTTL": 21600,
                    "ConcurrentExecutions": 100,
                    "Trigger": {
                        "Apigw": 10,
                        "Ckafka": 10,
                        "Clb": 10,
                        "Cls": 10,
                        "Cm": 10,
                        "Cmq": 10,
                        "Cos": 10,
                        "Eb": 10,
                        "Mps": 10,
                        "Timer": 10,
                        "Total": 110,
                        "Vod": 10
                    }
                }
            ]
        },
        "RequestId": "cvvdsds-af20-42a9-9314-84ad66b06ee4"
    }
}
```

