**Example 1: 成功**



Input: 

```
tccli adp DescribeAppTriggerRunLogList --cli-unfold-argument  \
    --AppId 2072866150944382336 \
    --FilterList.0.Name PushStatus \
    --FilterList.0.Operator 0 \
    --FilterList.0.ValueList 4 \
    --PageNumber 1 \
    --PageSize 10 \
    --TriggerId 64201696-52ee-49f6-a95b-0773b60a8e6b \
    --UserId cuiyo******
```

Output: 
```
{
    "Response": {
        "RunLogList": [
            {
                "ConversationId": "t2e41cd4a39cc455ea5308a543db8ac13",
                "DurationMs": "19106",
                "EndTime": "2026-07-03T10:41:44+08:00",
                "FireType": 3,
                "InstanceId": "2e41cd4a-39cc-455e-a530-8a543db8ac13",
                "PushStatus": 4,
                "ResultCode": "SUCCESS",
                "ResultSummary": "每隔 1 分钟执行 `hello` 工作流，对应的 **cron 表达式**为：\n\n```\n* * * * *\n```\n\n各字段含义（从左到右）：\n\n| 字段 | 值 | 含义 |\n|------|------|------|\n| 分钟 | `*` | 每分钟 |\n| 小时 | `*` | 每小时 |\n| 日 | `*` | 每天 |\n| 月 | `*` | 每月 |\n| 星期 | `*` | 每周任意一天 |\n\n---\n\n**常见平台的配置方式：**\n\n**1. Linux crontab**\n```bash\n* * * * * /path/to/hello_workflow.sh\n```\n\n**2. GitHub Actions**\n```yaml\non:\n  schedule:\n    - cron: '* * * * *'\n```\n\n**3. Kubernetes CronJob**\n```yaml\nspec:\n  schedule: '* * * * *'\n  jobTemplate:\n    spec:\n      template:\n        spec:\n          containers:\n            - name: hello\n              image: your-image\n              command: [\"./hello_workflow\"]\n```\n\n**4. Airflow DAG**\n```python\nfrom airflow import DAG\nfrom airflow.operators.bash import BashOperator\nfrom datetime import timedelta\n\ndefault_args = {\n    'start_date': datetime(2026, 7, 3),\n}\n\nwith DAG('hello_workflow',\n         schedule_interval=timedelta(minut",
                "RunId": "msg_a2583256-5c07-4e38-8992-6b49daf00d41_1",
                "ScheduledFireTime": "2026-07-03T10:41:24+08:00",
                "StartTime": "2026-07-03T10:41:24+08:00",
                "Status": 4,
                "TriggerId": "64201696-52ee-49f6-a95b-0773b60a8e6b",
                "Unread": true,
                "WorkflowRunId": ""
            }
        ],
        "TotalCount": "2",
        "RequestId": "121a757c-9765-4130-ac51-a8e2edce74c7"
    }
}
```

