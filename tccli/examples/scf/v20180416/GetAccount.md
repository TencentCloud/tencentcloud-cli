**Example 1: 获取账户信息**



Input: 

```
tccli scf GetAccount --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AccountLimit": {
            "Namespace": [
                {
                    "Trigger": {
                        "Cos": 2,
                        "Timer": 3,
                        "Ckafka": 2,
                        "Apigw": 2,
                        "Total": 11,
                        "Cmq": 2
                    },
                    "Namespace": "test01",
                    "ConcurrentExecutions": 20
                },
                {
                    "Trigger": {
                        "Cos": 2,
                        "Timer": 2,
                        "Ckafka": 2,
                        "Apigw": 2,
                        "Total": 10,
                        "Cmq": 2
                    },
                    "Namespace": "louiswu02-a8bb21",
                    "ConcurrentExecutions": 20
                },
                {
                    "Trigger": {
                        "Cos": 2,
                        "Timer": 2,
                        "Ckafka": 2,
                        "Apigw": 2,
                        "Total": 10,
                        "Cmq": 2
                    },
                    "Namespace": "louiswu02-606ce9",
                    "ConcurrentExecutions": 20
                },
                {
                    "Trigger": {
                        "Cos": 2,
                        "Timer": 2,
                        "Ckafka": 2,
                        "Apigw": 2,
                        "Total": 10,
                        "Cmq": 2
                    },
                    "Namespace": "louisw-f38e69",
                    "ConcurrentExecutions": 20
                },
                {
                    "Trigger": {
                        "Cos": 2,
                        "Timer": 2,
                        "Ckafka": 2,
                        "Apigw": 2,
                        "Total": 10,
                        "Cmq": 2
                    },
                    "Namespace": "kpk",
                    "ConcurrentExecutions": 20
                },
                {
                    "Trigger": {
                        "Cos": 2,
                        "Timer": 2,
                        "Ckafka": 2,
                        "Apigw": 2,
                        "Total": 10,
                        "Cmq": 2
                    },
                    "Namespace": "alanoluo",
                    "ConcurrentExecutions": 20
                },
                {
                    "Trigger": {
                        "Cos": 2,
                        "Timer": 2,
                        "Ckafka": 2,
                        "Apigw": 2,
                        "Total": 10,
                        "Cmq": 2
                    },
                    "Namespace": "12345",
                    "ConcurrentExecutions": 20
                }
            ],
            "NamespacesCount": 50
        },
        "RequestId": "627bff59-5c1d-43b1-99a8-c56c83b3e59f",
        "AccountUsage": {
            "Namespace": [
                {
                    "Functions": [
                        "testfun01",
                        "testfun02"
                    ],
                    "Namespace": "test01",
                    "FunctionsCount": 2
                },
                {
                    "Functions": [],
                    "Namespace": "louiswu02-a8bb21",
                    "FunctionsCount": 0
                },
                {
                    "Functions": [],
                    "Namespace": "louiswu02-606ce9",
                    "FunctionsCount": 0
                },
                {
                    "Functions": [
                        "louis06",
                        "louis05",
                        "louisw-f38e691",
                        "louisw-f38e69",
                        "louis04",
                        "louis02",
                        "louis01"
                    ],
                    "Namespace": "louisw-f38e69",
                    "FunctionsCount": 7
                },
                {
                    "Functions": [],
                    "Namespace": "kpk",
                    "FunctionsCount": 0
                },
                {
                    "Functions": [
                        "alano1",
                        "alanoluo_desc",
                        "ttstss"
                    ],
                    "Namespace": "alanoluo",
                    "FunctionsCount": 3
                },
                {
                    "Functions": [],
                    "Namespace": "12345",
                    "FunctionsCount": 0
                }
            ],
            "NamespacesCount": 7
        }
    }
}
```

