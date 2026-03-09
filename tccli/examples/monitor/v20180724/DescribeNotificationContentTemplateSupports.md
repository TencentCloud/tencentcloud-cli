**Example 1: 测试环境真实示例**



Input: 

```
tccli monitor DescribeNotificationContentTemplateSupports --cli-unfold-argument  \
    --MonitorType MT_QCE
```

Output: 
```
{
    "Response": {
        "RequestId": "4f48fd53-422b-469e-b467-bb5631f14656",
        "Support": {
            "Functions": null,
            "MonitorType": "MT_QCE",
            "Variables": [
                {
                    "Desc": "账号appid",
                    "Example": "123000456",
                    "Name": "{{.app_id}}"
                },
                {
                    "Desc": "控制台链接",
                    "Example": "腾讯云可观测平台告警详情页面链接",
                    "Name": "{{.console_link}}"
                },
                {
                    "Desc": "告警内容",
                    "Example": "CPU利用率 > 0%",
                    "Name": "{{.content}}"
                },
                {
                    "Desc": "当前等级（格式化）",
                    "Example": "提示 警告 严重",
                    "Name": "{{.current_level_fmt}}"
                },
                {
                    "Desc": "当前等级",
                    "Example": "None Note Warn Serious",
                    "Name": "{{.current_level}}"
                },
                {
                    "Desc": "当前数据",
                    "Example": "95.6% (CPU利用率)",
                    "Name": "{{.current_value_content}}"
                },
                {
                    "Desc": "持续时长（格式化）",
                    "Example": "5h4m3s",
                    "Name": "{{.duration_fmt}}"
                },
                {
                    "Desc": "持续时长 秒",
                    "Example": "1000",
                    "Name": "{{.duration}}"
                },
                {
                    "Desc": "首次触发时间（格式化）",
                    "Example": "2024-07-09 14:35:00 (UTC+08:00)",
                    "Name": "{{.first_trigger_time_fmt}}"
                },
                {
                    "Desc": "首次触发时间 秒",
                    "Example": "1732867259",
                    "Name": "{{.first_trigger_time}}"
                },
                {
                    "Desc": "上一次等级（格式化）",
                    "Example": "提示 警告 严重",
                    "Name": "{{.last_level_fmt}}"
                },
                {
                    "Desc": "上一次等级",
                    "Example": "None Note Warn Serious",
                    "Name": "{{.last_level}}"
                },
                {
                    "Desc": "小程序链接",
                    "Example": "腾讯云助手小程序云监控告警详情页面链接",
                    "Name": "{{.miniprogram_link}}"
                },
                {
                    "Desc": "告警对象",
                    "Example": "10.0.0.1 (内) | ins-123456 | as-tke-np-abc",
                    "Name": "{{.object}}"
                },
                {
                    "Desc": "告警策略ID",
                    "Example": "policy-abc123",
                    "Name": "{{.policy_id}}"
                },
                {
                    "Desc": "告警策略名称",
                    "Example": "腾讯云监控告警",
                    "Name": "{{.policy_name}}"
                },
                {
                    "Desc": "项目名称",
                    "Example": "默认",
                    "Name": "{{.project_name}}"
                },
                {
                    "Desc": "告警恢复时间（格式化）",
                    "Example": "2024-07-09 14:35:00 (UTC+08:00)",
                    "Name": "{{.recovery_time_fmt}}"
                },
                {
                    "Desc": "告警恢复时间 秒",
                    "Example": "1732867259",
                    "Name": "{{.recovery_time}}"
                },
                {
                    "Desc": "地域（格式化）",
                    "Example": "广州",
                    "Name": "{{.region_fmt}}"
                },
                {
                    "Desc": "地域",
                    "Example": "ap-guangzhou",
                    "Name": "{{.region}}"
                },
                {
                    "Desc": "云产品名称-策略类型",
                    "Example": "云服务器-基础监控",
                    "Name": "{{.server_name}}"
                },
                {
                    "Desc": "告警状态（格式化）",
                    "Example": "触发 恢复",
                    "Name": "{{.status_fmt}}"
                },
                {
                    "Desc": "告警状态和等级展示（格式化）",
                    "Example": "触发 持续 恢复 升级 降级",
                    "Name": "{{.status_level_fmt}}"
                },
                {
                    "Desc": "告警状态",
                    "Example": "Trigger Recovery",
                    "Name": "{{.status}}"
                },
                {
                    "Desc": "资源标签（格式化）",
                    "Example": "(业务部门:云监控)(功能:告警)",
                    "Name": "{{.tag_fmt}}"
                },
                {
                    "Desc": "告警策略提示",
                    "Example": "告警说明：基础CPU使用率是从母机采集到的数据。",
                    "Name": "{{.tooltip_text}}"
                },
                {
                    "Desc": "当前触发时间（格式化）",
                    "Example": "2024-07-09 14:35:00 (UTC+08:00)",
                    "Name": "{{.trigger_time_fmt}}"
                },
                {
                    "Desc": "当前触发时间 秒",
                    "Example": "1732867259",
                    "Name": "{{.trigger_time}}"
                }
            ]
        }
    }
}
```

