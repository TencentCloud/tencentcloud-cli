**Example 1: 查询事件列表**



Input: 

```
tccli monitor DescribeAlarmEvents --cli-unfold-argument  \
    --Module monitor \
    --Namespace cvm_device \
    --MonitorType MT_QCE
```

Output: 
```
{
    "Response": {
        "RequestId": "92hg92hj1-2h352h25hj-2h235h",
        "Events": [
            {
                "EventName": "ping_unreachable",
                "Description": "ping不可达",
                "Namespace": "cvm_device"
            }
        ]
    }
}
```

