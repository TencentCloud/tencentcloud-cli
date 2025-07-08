**Example 1: 1**



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
            "AccessKeyRemark": "飞快的云镜-临时密钥",
            "AlarmRuleID": 10969,
            "AlarmType": 0,
            "AppID": 1256299843,
            "Date": "2025-02-26",
            "ID": 10007,
            "LastAlarmTime": "2025-02-26 23:50:04",
            "Level": 4,
            "Name": "非控制台方式调用高危接口",
            "Nickname": "飞快的云镜",
            "Status": 0,
            "SubNickname": "飞快的云镜",
            "SubUin": "100004506473",
            "Tag": [],
            "Type": 2,
            "Uin": "100004506473"
        },
        "CamCount": 1111,
        "RequestId": "e33bc9ad-0496-49de-a76b-940f2d6027bb",
        "RiskCount": 0
    }
}
```

