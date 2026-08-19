**Example 1: 1**



Input: 

```
tccli csip DescribeAIScheduleList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Status 0 \
    --ScheduleId a156***************************29702
```

Output: 
```
{
    "Response": {
        "ScheduleSet": [
            {
                "CreateTime": 1776841342887,
                "CurrentFireCount": 0,
                "EndTime": 0,
                "Identity": {
                    "AppId": 260083796,
                    "BotId": "aibn2Vz1_iZ1R2B5mGjZ5o9ph3SmfjdLEQO",
                    "Channel": "wecom",
                    "ChatId": "T70030002A",
                    "SubUin": "",
                    "Uin": "700002365149",
                    "UserId": "T70030002A"
                },
                "MaxFireCount": 0,
                "Name": "CSIP周报定时发送",
                "Prompts": "生成云安全中心周报，整理成PDF和PPT，通过email技能发送到rainewang@tencent.com",
                "ScheduleId": "586ecd9e-d140-45bb-889e-3476efaa4b50",
                "StartTime": 0,
                "Status": 1,
                "Triggers": [
                    {
                        "TriggerId": "8a09c63b-a324-4707-a0e5-3a6722c20da1",
                        "TriggerType": 1
                    }
                ],
                "UpdateTime": 1776841342887
            }
        ],
        "TotalCount": 7,
        "RequestId": "666d1958-ca82-47a4-b3d9-dd49b2caa6c8"
    }
}
```

