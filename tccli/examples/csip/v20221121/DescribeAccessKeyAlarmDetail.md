**Example 1: 访问密钥告警记录详情**



Input: 

```
tccli csip DescribeAccessKeyAlarmDetail --cli-unfold-argument  \
    --ID 10007
```

Output: 
```
{
    "Response": {
        "AlarmInfo": {
            "AccessKey": "TEMP_AK",
            "AccessKeyID": 10093,
            "AccessKeyRemark": "临时密钥",
            "AlarmRuleID": 10969,
            "AlarmType": 0,
            "AppID": 100001,
            "Date": "2025-02-26",
            "ID": 10007,
            "LastAlarmTime": "2025-02-26 23:50:04",
            "Level": 4,
            "Name": "非控制台方式调用高危接口",
            "Nickname": "name",
            "Status": 0,
            "SubNickname": "name",
            "SubUin": "1000045***",
            "Tag": [],
            "Type": 2,
            "Uin": "1000045***"
        },
        "CamCount": 10,
        "RequestId": "e33bc9ad-0496-49de-a76b-940f2d6027bb",
        "RiskCount": 0
    }
}
```

