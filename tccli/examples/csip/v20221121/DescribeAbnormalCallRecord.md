**Example 1: 获取调用记录列表**



Input: 

```
tccli csip DescribeAbnormalCallRecord --cli-unfold-argument  \
    --AlarmRuleID 10007 \
    --Filter.Limit 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AccessKey": "AKID*******",
                "AccessKeyID": 10093,
                "AccessKeyRemark": "临时密钥",
                "AppID": 100001,
                "CallCount": 50,
                "CallID": "13",
                "Code": 0,
                "Date": "2025-02-26 00:00:00",
                "EventName": "ListAccessKeys",
                "EventType": 1,
                "FirstCallTime": "2025-02-26 23:37:59",
                "IPType": 1,
                "InstanceID": "",
                "InstanceName": "",
                "LastCallTime": "2025-02-26 23:39:46",
                "PolicySet": [],
                "ProductName": "cam",
                "Region": "",
                "SourceIP": "30.49.109.***",
                "SourceIPRemark": "",
                "UserName": "1000246***",
                "UserType": "AssumedRole"
            }
        ],
        "RequestId": "1a431738-b670-4c86-94c1-cae98e11af64",
        "Total": 2
    }
}
```

