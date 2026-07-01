**Example 1: DescribeEdrAlertInfo**

获取EDR告警详情

Input: 

```
tccli csip DescribeEdrAlertInfo --cli-unfold-argument  \
    --Target.Id 1000000000004319 \
    --Target.AppId 260108008 \
    --Target.AlertId 2e44dee79d7d98335f2c2ec5c33aaf0a \
    --Target.Quuid 8a4eac2e-d5e0-4422-8ab1-5199ccffd9c0 \
    --Target.InstanceId ins-llfob98q
```

Output: 
```
{
    "Response": {
        "Alert": {
            "AlertCategory": "AI_LINK_ENGINE",
            "AlertId": "2e44dee79d7d98335f2c2ec5c33aaf0a",
            "AlertName": "多行为攻击",
            "AlertSource": "HOST",
            "AlertSubType": "MULTI_BEHAVIOR_ATTACK",
            "AppId": 260108008,
            "AttackStage": "",
            "CSIPTags": [],
            "ClusterId": "",
            "ContainerId": "",
            "Content": "{\"alert_raw_id\":\"eql-333a7b877fc181df\",\"alert_raw_ids\":[\"eql-333a7b877fc181df\"],\"alert_source_engine\":\"AI-Link\",\"alert_source_rule_mode\":\"balanced\",\"alert_type_category\":\"command\",\"behaviors\":[{\"action\":\"process_snapshot\",\"behavior_description\":\"bash DNS process_snapshot a.qqmusic1.com\",\"behavior_description_en\":\"bash DNS process_snapshot a.qqmusic1.com\",\"dataset\":\"cwp.dns\",\"destination_ip\":\"13.158.37.189\",\"dns_question_name\":\"a.qqmusic1.com\",\"parent_process_cmdline\":\"\",\"parent_process_name\":\"\",\"process_command_line\":\"/bin/sh -c sleep 100\",\"process_executable\":\"bash\",\"process_md5\":\"4002e96f27590cee08ca6bf6d32db707\",\"process_name\":\"bash\",\"process_pid\":62635,\"process_start\":\"\",\"pstree\":\"[{\\\"exe\\\":\\\"bash\\\",\\\"cmdline\\\":\\\"/bin/sh -c sleep 100\\\",\\\"pid\\\":62635,\\\"name\\\":\\\"bash\\\"}]\",\"threat_intels\":[{\"field\":\"dns_question_name\",\"ioc_type\":\"domain\",\"ioc_value\":\"a.qqmusic1.com\",\"domain_detail\":{\"Result\":\"black\",\"Basis\":[\"情报分析\"],\"RegistrarName\":\"redacted for privacy\",\"DNSHistory\":[{\"IP\":\"47.238.142.66\",\"Tags\":[\"ValleyRAT远控木马\",\"Winos4.0恶意软件\",\"树狼远控木马\",\"银狐组织\"],\"Location\":[\"中国\",\"中国香港\",\"中国香港\"],\"ISP\":\"阿里云\",\"FirstSeen\":\"2026-01-28 05:54:05\",\"LastSeen\":\"2026-05-31 17:06:04\"},{\"IP\":\"8.217.103.109\",\"Tags\":[\"代理秒拨\"],\"Location\":[\"中国\",\"中国香港\",\"中国香港\"],\"ISP\":\"阿里云\",\"FirstSeen\":\"2026-04-14 15:48:00\",\"LastSeen\":\"2026-05-01 05:05:02\"},{\"IP\":\"47.75.116.189\",\"Tags\":[\"ValleyRAT远控木马\",\"Winos4.0恶意软件\",\"银狐组织\"],\"Location\":[\"中国\",\"中国香港\",\"中国香港\"],\"ISP\":\"阿里云\",\"FirstSeen\":\"2026-05-30 10:02:11\",\"LastSeen\":\"2026-05-30 10:02:11\"}]}},{\"field\":\"destination_ip\",\"ioc_type\":\"ip\",\"ioc_value\":\"13.158.37.189\",\"ip_detail\":{\"Result\":\"suspicious\",\"Tags\":[\"银狐组织\",\"代理秒拨\"],\"Basis\":\"情报分析\",\"ISP\":\"亚马逊\",\"Location\":[\"日本\",\"东京都\",\"东京\"],\"Family\":[\"银狐\"],\"Purpose\":[\"IDC-IP\"],\"Referer\":[{\"Domain\":\"uu.goldeyeuu.io\",\"Tags\":[\"Zusy银行木马\"],\"Time\":\"2026-05-27 00:00:00\"},{\"Domain\":\"wk.goldeyeuu.io\",\"Tags\":[\"Zusy银行木马\"],\"Time\":\"2026-05-27 00:00:00\"}]}}],\"timestamp\":\"2026-05-26T06:06:47.134112932+08:00\",\"user_name\":\"root\",\"working_directory\":\"\"}],\"edr_rule_id\":\"rule-c24e613eff9b86d9\",\"edr_rule_name\":\"多字段测试规则-宽列滚动\",\"execute_user\":\"root\",\"harm_description\":\"黑客在入侵服务器后，为了进行下一步的恶意操作，会执行恶意文件下载、连接矿池、添加公钥、查看敏感文件等操作。\",\"suggest_scheme\":\"1.检查恶意进程及非法端口，删除可疑的启动项和定时任务；2.隔离或者删除相关的木马文件；3.对系统进行风险排查，并进行安全加固\"}",
            "ContentType": "",
            "DetectMode": "BALANCED",
            "EventCount": 1,
            "FirstDetectTime": "2026-05-25 14:52:56",
            "HarmDesc": "黑客在入侵服务器后，为了进行下一步的恶意操作，会执行恶意文件下载、连接矿池、添加公钥、查看敏感文件等操作。",
            "HarmDescSource": "default",
            "Id": 1000000000004319,
            "ImageId": "",
            "InstanceId": "ins-llfob98q",
            "InstanceName": "",
            "IntelSource": "",
            "IsProVersion": 1,
            "LatestDetectTime": "2026-05-25 14:52:56",
            "Level": "MEDIUM",
            "ModifyTime": "2026-05-28 17:38:45",
            "MultiBehaviorDetectionMode": "command",
            "PrivateIp": "",
            "PublicIp": "",
            "Quuid": "8a4eac2e-d5e0-4422-8ab1-5199ccffd9c0",
            "RuleId": "908776",
            "RuleName": "",
            "RuleType": 0,
            "SourceDesc": "规则引擎: AI-Link 智链引擎\n规则 908776\n检测模式: 均衡",
            "Status": "PENDING",
            "SuggestScheme": "1.检查恶意进程及非法端口，删除可疑的启动项和定时任务；2.隔离或者删除相关的木马文件；3.对系统进行风险排查，并进行安全加固",
            "ThreatTags": [],
            "Verdict": "",
            "VerdictBasis": ""
        },
        "RequestId": "f8998684-7376-4fcf-9c6d-4f20dd0591a0"
    }
}
```

