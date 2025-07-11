**Example 1: 1**



Input: 

```
tccli csip DescribeAccessKeyAlarm --cli-unfold-argument  \
    --Filter.Limit 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AccessKey": "TEMP_AK",
                "AccessKeyID": 10093,
                "AccessKeyRemark": "飞快的云镜-临时密钥",
                "AlarmRuleID": 94865,
                "AlarmType": 0,
                "AppID": 1256299843,
                "Date": "2025-03-13",
                "ID": 10185,
                "LastAlarmTime": "2025-03-13 16:50:44",
                "Level": 5,
                "Name": "可疑IP调用高危接口",
                "Nickname": "飞快的云镜",
                "Status": 0,
                "SubNickname": "飞快的云镜",
                "SubUin": "100004506473",
                "Tag": [],
                "Type": 2,
                "Uin": "100004506473"
            }
        ],
        "RequestId": "1249df92-930b-4574-a517-45dc70580764",
        "Total": 28
    }
}
```

