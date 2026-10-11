**Example 1: 云产品监控详情页示例**



Input: 

```
tccli monitor DescribeAlarmNotifyHistories --cli-unfold-argument  \
    --MonitorType MT_QCE \
    --QueryBaseTime 1791445402 \
    --QueryBeforeSeconds 3600 \
    --PageParams.PerPage 20 \
    --PageParams.PageNo 1 \
    --NotifyId f29a30fb731ba2c5c2afaf0379e40201_c**hs
```

Output: 
```
{
    "Response": {
        "AlarmNotifyHistoryList": [
            {
                "AlarmContent": "CPU利用率 > 0%",
                "AlarmObject": "172.16.0.45 (内)  | ins-3vpoml9k | chengming-勿删勿动-长期使用（研发大佬请用） | vpcId: vpc-4wyuws75",
                "ChannelSet": [
                    "QCloudYehe_email"
                ],
                "ChannelsReceivers": [
                    {
                        "ChannelName": "QCloudYehe",
                        "Contents": [
                            {
                                "Content": "【TCOP】【告警触发】云产品告警详情页测试\n尊敬的腾讯云用户，您好！\n\n       您的腾讯云账号（账号ID：1500000686，昵称：686_nickname）的云产品监控告警触发。\n\n告警内容：云服务器-基础监控 | CPU利用率 > 0% \n告警对象：172.16.0.45 (内)  | ins-3vpoml9k | chengming-勿删勿动-长期使用（研发大佬请用） | vpcId: vpc-4wyuws75\n当前数据：0.85% (CPU利用率)\n项目|地域：默认项目 | 广州\nAPPID：251005942\n告警策略：云产品告警详情页测试\n触发时间：2026-10-08 16:49:00 (UTC+08:00)\n告警说明：CPU 利用率过高会容易引起服务响应速度变慢、服务器登录不上等问题。可能由硬件、系统进程、业务进程或者木马病毒等因素所致。详见排查指引https://cloud.tencent.com/document/product/248/44698 \n\n此致 \n腾讯云团队",
                                "SubChannel": "QCloudYehe_email"
                            }
                        ],
                        "ExecDetail": "",
                        "RealDeliverErrMsg": "",
                        "RealDeliverStatus": "",
                        "RealDeliverTime": "",
                        "Receivers": [
                            "906911493"
                        ],
                        "SendStatus": "NotifyChannelExecSucc",
                        "SendStatusCode": "OK_0",
                        "SendTime": 1791449424,
                        "SubChannels": [
                            "QCloudYehe_email"
                        ]
                    }
                ],
                "Labels": [
                    {
                        "Name": "BaradAlarm_appid",
                        "Value": "251005942"
                    }
                ],
                "Notices": [
                    {
                        "NoticeId": "notice-67tqbxsn",
                        "NoticeName": "系统预设通知模板"
                    }
                ],
                "NotifyId": "f29a30fb731ba2c5c2afaf0379e40201_c29hs",
                "NotifyTime": 1791449424,
                "PolicyId": "policy-6a7jmi0d",
                "PolicyName": "云产品告警详情页测试",
                "PromeConsoleURL": "",
                "PromeInstanceID": "",
                "PromeInstanceRegion": "",
                "ReceiverGroups": [
                    {
                        "ChannelNames": [
                            "QCloudYehe_email"
                        ],
                        "DayEndSeconds": 86399,
                        "DayStartSeconds": 0,
                        "MemberIds": null,
                        "Names": [
                            "log_test2"
                        ],
                        "ReceiverIds": [
                            "906911493"
                        ],
                        "ReceiverType": "UIDs",
                        "TimeZoneName": "",
                        "WeekDay": [
                            0
                        ]
                    }
                ],
                "SessionId": "r_gz_2149202746_13c263af2fd1a2ef8cea0f3a7609a29f_65041",
                "TriggerLevel": "None",
                "TriggerStatus": "Trigger",
                "TriggerTime": 1791449340
            }
        ],
        "PageResult": {
            "CurrentPageNo": 1,
            "IsEnd": true,
            "TotalCount": 1,
            "TotalPage": 1
        },
        "RequestId": "e33f23d5-da28-45fb-91db-9ccecd0793d3"
    }
}
```

