**Example 1: 查询Prometheus通知历史**



Input: 

```
tccli monitor DescribeAlarmNotifyHistories --cli-unfold-argument  \
    --MonitorType MT_PROME \
    --QueryBaseTime 1734576676 \
    --QueryBeforeSeconds 172000 \
    --PageParams.PerPage 1 \
    --PageParams.PageNo 1
```

Output: 
```
{
    "Response": {
        "AlarmNotifyHistoryList": [
            {
                "AlarmContent": "这是消息体\n这是消息体第二行\n<font color=\"green\">这是绿色的消息体</font>",
                "AlarmObject": "新amp接口告警",
                "ChannelSet": [
                    "DingDing",
                    "FeiShu",
                    "WeWork",
                    "WebHook"
                ],
                "ChannelsReceivers": [
                    {
                        "ChannelName": "DingDing",
                        "Receivers": [
                            "https://oapi.dingtalk.com/robot/send?access_token=c1090c31391e5766b6e509d6ed0ac9930447231f8c151a5b8aa61ffb637db3ec"
                        ],
                        "SendStatus": "NotifyChannelExecSucc"
                    },
                    {
                        "ChannelName": "FeiShu",
                        "Receivers": [
                            "https://open.feishu.cn/open-apis/bot/v2/hook/58151696-a863-47e8-ae49-dfa982e48b25"
                        ],
                        "SendStatus": "NotifyChannelExecSucc"
                    },
                    {
                        "ChannelName": "QCloudYehe",
                        "Receivers": [
                            "907876075",
                            "906793755"
                        ],
                        "SendStatus": "NotifyChannelExecSucc"
                    },
                    {
                        "ChannelName": "WeWork",
                        "Receivers": [
                            "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=12d11141-d6e8-44df-b00e-03285ad65415"
                        ],
                        "SendStatus": "NotifyChannelExecSucc"
                    },
                    {
                        "ChannelName": "WebHook",
                        "Receivers": [
                            "http://118.24.173.149:9090/test/sendAlerts"
                        ],
                        "SendStatus": "NotifyChannelExecSucc"
                    }
                ],
                "Notices": [
                    {
                        "NoticeId": "notice-625w0q92",
                        "NoticeName": "Prom通知测试企微机器人"
                    }
                ],
                "NotifyId": "b476ba3696525213f0c88033e56e8675_c1u82",
                "NotifyTime": 1734497292,
                "PolicyId": "alert-p8yurlq0",
                "PolicyName": "能收到吗/aaaaa",
                "PromeInstanceID": "prom-pysf4frm",
                "PromeInstanceRegion": "ap-guangzhou",
                "SessionId": "prom-pysf4frm_3ef6b8b216aa56e9",
                "TriggerLevel": "Invalid",
                "TriggerStatus": "Recovery",
                "TriggerTime": 1734491764
            }
        ],
        "PageResult": {
            "CurrentPageNo": 1,
            "IsEnd": false,
            "TotalCount": 19,
            "TotalPage": 19
        },
        "RequestId": "efc734bb-1caa-4a4f-a159-97115b57125a"
    }
}
```

