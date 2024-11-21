**Example 1: DescribeUnHandleEventTabList**



Input: 

```
tccli cfw DescribeUnHandleEventTabList --cli-unfold-argument  \
    --EndTime 2021-05-206 23:59:59 \
    --StartTime 2021-05-20 00:00:00 \
    --AssetID ins-0752de63
```

Output: 
```
{
    "Response": {
        "Data": {
            "EventTableListStruct": [
                {
                    "EventName": "主机失陷",
                    "Total": 3
                },
                {
                    "EventName": "安全基线（出）",
                    "Total": 2635
                }
            ],
            "BaseLineUser": 1,
            "BaseLineInSwitch": 1,
            "BaseLineOutSwitch": 1
        },
        "RequestId": "0752de63-570c-4c2e-bbd2-78574e22a1ae",
        "ReturnCode": 0,
        "ReturnMsg": "sccuess"
    }
}
```

