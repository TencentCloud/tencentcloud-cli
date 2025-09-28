**Example 1: 查询慢日志详情**



Input: 

```
tccli mongodb DescribeDetailedSlowLogs --cli-unfold-argument  \
    --InstanceId cmgo-r3p8**** \
    --StartTime 2025-09-22 11:53:15 \
    --EndTime 2025-09-23 11:53:15
```

Output: 
```
{
    "Response": {
        "DetailedSlowLogs": [
            {
                "Log": "Mon Sep 22 20:30:19.980 I COMMAND  [conn3725696] command admin.$cmd command: saslContinue { saslContinue: 1, conversationId: 1, payload: BinData(0, ), $clusterTime: { clusterTime: Timestamp(1758544211, 1), signature: { hash: BinData(0, C28B5E1C1EE29**************************), keyId: 75428892796********* } }, $db: \"admin\", $readPreference: { mode: \"primaryPreferred\" } } numYields:0 reslen:204 locks:{} protocol:op_msg 184ms",
                "NodeName": "cmgo-r3p8****_0-node-primary",
                "QueryHash": "admin..****Continue"
            }
        ],
        "RequestId": "5e35a1bd-60e6-4a45-8792-d033581b9209",
        "TotalCount": 1
    }
}
```

