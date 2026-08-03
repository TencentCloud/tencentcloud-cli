**Example 1: 成功**



Input: 

```
tccli adp DescribeAppTriggerInstance --cli-unfold-argument  \
    --AppId 2072866150944382336 \
    --InstanceId 2e41cd4a-39cc-455e-a530-8a543db8ac13 \
    --UserId cuiyo******
```

Output: 
```
{
    "Response": {
        "Instance": {
            "AppId": "2072866150944382336",
            "ConversationId": "t2e41cd4a39cc455ea5308a543db8ac13",
            "CreatedAt": "2026-07-03T10:41:24+08:00",
            "FinishedAt": "2026-07-03T10:41:44+08:00",
            "InstanceId": "2e41cd4a-39cc-455e-a530-8a543db8ac13",
            "RequestId": "trigger_2e41cd4a-39cc-455e-a530-8a543db8ac13",
            "ResultCode": "SUCCESS",
            "ResultSummary": "每隔 1 分钟执行 `hello` 工作流，对应的 **cron 表达式**为：\n\n```\n* * * * *\n```\n\n各字段含义（从左到右）：\n\n| 字段 | 值 | 含义 |\n|------|------|------|\n| 分钟 | `*` | 每分钟 |\n| 小时 | `*` | 每小时 |\n| 日 | `*` | 每天 |\n| 月 | `*` | 每月 |\n| 星期 | `*` | 每周任意一天 |\n\n---\n\n**常见平台的配置方式：**\n\n**1. Linux crontab**\n```bash\n* * * * * /path/to/hello_workflow.sh\n```\n\n**2. GitHub Actions**\n```yaml\non:\n  schedule:\n    - cron: '* * * * *'\n```\n\n**3. Kubernetes CronJob**\n```yaml\nspec:\n  schedule: '* * * * *'\n  jobTemplate:\n    spec:\n      template:\n        spec:\n          containers:\n            - name: hello\n              image: your-image\n              command: [\"./hello_workflow\"]\n```\n\n**4. Airflow DAG**\n```python\nfrom airflow import DAG\nfrom airflow.operators.bash import BashOperator\nfrom datetime import timedelta\n\ndefault_args = {\n    'start_date': datetime(2026, 7, 3),\n}\n\nwith DAG('hello_workflow',\n         schedule_interval=timedelta(minut",
            "RunId": "msg_a2583256-5c07-4e38-8992-6b49daf00d41_1",
            "Source": 1,
            "StartedAt": "2026-07-03T10:41:24+08:00",
            "Status": 4,
            "TraceId": "121b84421b74a353eba6a0a793232925 / rcd_a2583256-5c07-4e38-8992-6b49daf00d41",
            "TriggerId": "64201696-52ee-49f6-a95b-0773b60a8e6b",
            "WorkflowRunId": ""
        },
        "RequestId": "d32dd79b-5346-4cbe-8d0e-dd789a986116"
    }
}
```

