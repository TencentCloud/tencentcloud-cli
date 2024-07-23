**Example 1: 查询参数模板详情**



Input: 

```
tccli mongodb DescribeDBInstanceParamTplDetail --cli-unfold-argument  \
    --TplId tpl-2284g3nmw
```

Output: 
```
{
    "Response": {
        "ClusterType": "REPLSET",
        "InstanceEnumParams": [
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
                "Status": 1,
                "Tips": [
                    "",
                    "specifies which operations should be profiled."
                ],
                "ValueType": "enum"
            },
            {
                "CurrentValue": "snappy",
                "DefaultValue": "snappy",
                "EnumValue": [
                    "snappy",
                    "zlib",
                    "zstd",
                    "none"
                ],
                "NeedRestart": "1",
                "ParamName": "storage.wiredTiger.collectionConfig.blockCompressor",
                "Status": 1,
                "Tips": [
                    "",
                    "you can uses zstd for journal compression and data compression."
                ],
                "ValueType": "enum"
            }
        ],
        "InstanceIntegerParams": [
            {
                "CurrentValue": "100",
                "DefaultValue": "100",
                "Max": "65536",
                "Min": "0",
                "NeedRestart": "0",
                "ParamName": "operation.profiling.slowOpThresholdMs",
                "Status": 1,
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
                "Status": 1,
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
                "ParamName": "setParameter.internalQueryMaxBlockingSortMemoryUsageBytes",
                "Status": 1,
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
                "Status": 1,
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
                "Status": 1,
                "Tips": [
                    "",
                    "specifies the lifetime of multi-document transactions."
                ],
                "Unit": "",
                "ValueType": "integer"
            }
        ],
        "InstanceMultiParams": [],
        "InstanceTextParams": [],
        "MongoVersion": "MONGO_50_WT",
        "RequestId": "5dedc31c-ee80-4a12-9ed3-6003504b5a57",
        "TotalCount": 7,
        "TplName": "demo"
    }
}
```

