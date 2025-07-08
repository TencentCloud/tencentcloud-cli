**Example 1: 1**



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
                "AccessKey": "AKID6*******tZBU1Hi",
                "AccessKeyID": 10093,
                "AccessKeyRemark": "飞快的云镜-临时密钥",
                "AppID": 1256299843,
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
                "SourceIP": "30.49.109.154",
                "SourceIPRemark": "",
                "UserName": "100024699394",
                "UserType": "AssumedRole"
            }
        ],
        "RequestId": "1a431738-b670-4c86-94c1-cae98e11af64",
        "Total": 2
    }
}
```

