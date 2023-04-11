**Example 1: InstanceEnumParam**

用户请求该接口获取其mongoDB实例可配置的参数列表；

Input: 

```
tccli mongodb DescribeInstanceParams --cli-unfold-argument  \
    --InstanceId cmgo-9d0p****
```

Output: 
```
{
    "Response": {
        "InstanceEnumParam": [
            {
                "CurrentValue": "off",
                "DefaultValue": "off",
                "EnumValue": [
                    "off",
                    "slowOp",
                    "all"
                ],
                "NeedRestart": "0",
                "ParamName": "operationProfiling.mode",
                "Status": 0,
                "Tips": [
                    "",
                    "specifies which operations should be profiled."
                ],
                "ValueType": "enum"
            },
            {
                "CurrentValue": "true",
                "DefaultValue": "true",
                "EnumValue": [
                    "true",
                    "false"
                ],
                "NeedRestart": "0",
                "ParamName": "setParameter.failIndexKeyTooLong",
                "Status": 0,
                "Tips": [
                    "",
                    "index key length limit applies."
                ],
                "ValueType": "enum"
            }
        ],
        "InstanceIntegerParam": [
            {
                "CurrentValue": "100",
                "DefaultValue": "100",
                "Max": "65536",
                "Min": "0",
                "NeedRestart": "0",
                "ParamName": "operation.profiling.slowOpThresholdMs",
                "Status": 0,
                "Tips": [
                    "",
                    "the slow operation time threshold, in milliseconds."
                ],
                "Unit": "",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "600000",
                "DefaultValue": "600000",
                "Max": "2147483647",
                "Min": "1",
                "NeedRestart": "0",
                "ParamName": "setParameter.cursorTimeoutMillis",
                "Status": 0,
                "Tips": [
                    "",
                    "sets the expiration threshold in milliseconds for idle cursors before MongoDB removes them."
                ],
                "Unit": "",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "33554432",
                "DefaultValue": "33554432",
                "Max": "268435456",
                "Min": "33554432",
                "NeedRestart": "0",
                "ParamName": "setParameter.internalQueryExecMaxBlockingSortBytes",
                "Status": 0,
                "Tips": [
                    "",
                    "internal query exec max blocking sort bytes."
                ],
                "Unit": "",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "5",
                "DefaultValue": "5",
                "Max": "60",
                "Min": "0",
                "NeedRestart": "0",
                "ParamName": "setParameter.maxTransactionLockRequestTimeoutMillis",
                "Status": 0,
                "Tips": [
                    "",
                    "the maximum amount of time in milliseconds that multi-document transactions should wait to acquire locks required by the operations in the transaction."
                ],
                "Unit": "",
                "ValueType": "integer"
            },
            {
                "CurrentValue": "60",
                "DefaultValue": "60",
                "Max": "300",
                "Min": "5",
                "NeedRestart": "0",
                "ParamName": "setParameter.transactionLifetimeLimitSeconds",
                "Status": 0,
                "Tips": [
                    "",
                    "specifies the lifetime of multi-document transactions."
                ],
                "Unit": "",
                "ValueType": "integer"
            }
        ],
        "InstanceMultiParam": [],
        "InstanceTextParam": [],
        "RequestId": "c07728e2-6747-4b0f-bcc9-e022036d5e28",
        "TotalCount": 7
    }
}
```

