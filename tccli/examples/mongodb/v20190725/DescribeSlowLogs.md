**Example 1: 获取实例慢日志信息**

以下示例为获取一实例的慢日志信息。

Input: 

```
tccli mongodb DescribeSlowLogs --cli-unfold-argument  \
    --InstanceId cmgo-r3p8**** \
    --StartTime 2025-09-22 00:00:00 \
    --EndTime 2025-09-23 00:00:00 \
    --SlowMS 100 \
    --Offset 1 \
    --Limit 1 \
    --Format json
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "RequestId": "ec514cb8-55a6-41d4-a6e4-896da43886db",
        "SlowLogs": [
            "Mon Sep 22 20:30:19.980 I COMMAND  [conn3725696] command admin.$cmd command: ****Continue { ****Continue: 1, conversationId: 1, payload: BinData(0, ), $clusterTime: { clusterTime: Timestamp(1758544211, 1), signature: { hash: BinData(0, *************************************), keyId: 7542889************ } }, $db: \"admin\", $readPreference: { mode: \"primaryPreferred\" } } numYields:0 reslen:204 locks:{} protocol:op_msg 184ms"
        ]
    }
}
```

