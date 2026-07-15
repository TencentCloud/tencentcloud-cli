**Example 1: demo**



Input: 

```
tccli oceanus DescribeJobEvents --cli-unfold-argument  \
    --JobId cql-719492aj \
    --StartTimestamp 1776360360 \
    --EndTimestamp 1778952360 \
    --Types 1 \
    --RunningOrderIds 2041 \
    --WorkSpaceId space-niu92ssm \
    --Limit 50 \
    --Offset 50
```

Output: 
```
{
    "Response": {
        "Events": [
            {
                "CauseAnalysis": "",
                "Description": "发生作业失败",
                "Message": "作业从 RUNNING 状态变为 RESTARTING 状态，异常消息：org.apache.flink.kafka.shaded.org.apache.kafka.common.errors.IllegalSaslStateException: Unexpected handshake request with client mechanism PLAIN, enabled mechanisms are []\n",
                "RunningOrderId": 2038,
                "Solution": "",
                "SolutionLink": "https://cloud.tencent.com/document/product/849/64499",
                "Timestamp": 1778751035,
                "Type": "21"
            }
        ],
        "RunningOrderIds": [],
        "TotalCount": 21371,
        "Versions": null,
        "RequestId": "483f0637-17f5-468d-b140-85ff554053cb"
    }
}
```

