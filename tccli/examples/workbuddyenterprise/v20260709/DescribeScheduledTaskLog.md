**Example 1: 查询执行日志详情**

按 TaskId + LogId 查询单条执行日志详情（示例为部分成功 + 投递失败场景，所有字段均有值）

Input: 

```
tccli workbuddyenterprise DescribeScheduledTaskLog --cli-unfold-argument  \
    --TaskId 736918400000000001 \
    --LogId 736919300000000001
```

Output: 
```
{
    "Response": {
        "LogId": "736919300000000001",
        "TaskId": "736918400000000001",
        "TaskKey": "task_daily_report",
        "SessionId": "sess_a1b2c3d4",
        "SessionName": "每日日报",
        "TriggerType": "CRON",
        "Status": "PARTIAL",
        "Prompt": "请汇总今日数据并生成日报",
        "Result": "今日汇总如下：一、运营数据……二、告警概览……",
        "ErrorMessage": "上游模型调用部分超时，已输出 3/5 个板块",
        "StartTime": "2026-09-18 10:00:00",
        "EndTime": "2026-09-18 10:00:05",
        "DurationMs": 5000,
        "DeliveryStatus": "FAILED",
        "DeliveryError": "企微群机器人 Webhook 返回 410 Gone，请更新机器人配置",
        "CreatedTime": "2026-09-18 10:00:00",
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

