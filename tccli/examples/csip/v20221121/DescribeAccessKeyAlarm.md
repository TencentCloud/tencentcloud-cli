**Example 1: 访问密钥告警记录列表**



Input: 

```
tccli csip DescribeAccessKeyAlarm --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AccessKey": "TEMP_AK",
                "AccessKeyID": 10093,
                "AccessKeyRemark": "临时密钥",
                "AlarmRuleID": 94865,
                "AlarmType": 0,
                "AppID": 1200001,
                "Date": "2025-03-13",
                "ID": 10185,
                "LastAlarmTime": "2025-03-13 16:50:44",
                "Level": 5,
                "Name": "可疑IP调用高危接口",
                "Nickname": "name",
                "Status": 0,
                "SubNickname": "name",
                "SubUin": "10000**",
                "Tag": [],
                "Type": 2,
                "Uin": "10000**"
            }
        ],
        "RequestId": "1249df92-930b-4574-a517-45dc70580764",
        "Total": 1
    }
}
```

