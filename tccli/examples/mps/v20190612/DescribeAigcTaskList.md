**Example 1: 查询任务列表接口-按任务ID过滤**

按任务ID过滤

Input: 

```
tccli mps DescribeAigcTaskList --cli-unfold-argument  \
    --QueryTaskFilter.TaskId 5ddc84c0-fe47-4cc8-35b8-ae8c313d1b9e
```

Output: 
```
{
    "Response": {
        "PageNum": 1,
        "PageSize": 10,
        "Tasks": [
            {
                "CreateTime": "2026-05-26 20:19:49",
                "FinishedTime": "2026-05-26 20:27:08",
                "RequestBody": "\"{\\\"Input\\\":{\\\"Url\\\":\\\"https://lewis-1302487817.cos.ap-guangzhou.myqcloud.com/replace-test/1s.mp4\\\"},\\\"Action\\\":\\\"CreateVideoRedrawTask\\\",\\\"RequestId\\\":\\\"3a35e21a-f31a-4a49-983f-0b7fc4ab5214\\\",\\\"Uin\\\":\\\"600000563781\\\",\\\"ApiModule\\\":\\\"mps\\\",\\\"Region\\\":\\\"\\\",\\\"AppId\\\":1300057355}\"",
                "ScheduledTime": "2026-05-26 20:19:50",
                "TaskId": "5ddc84c0-fe47-4cc8-35b8-ae8c313d1b9e",
                "TaskStatus": "FINISHED",
                "TaskType": "RedrawVideo",
                "Urls": [
                    "https://aigc-redraw-output-1311402212.cos.ap-guangzhou.myqcloud.com/5ddc84c0-fe47-4cc8-35b8-ae8c313d1b9e/redraw_output.mp4?q-sign-algorithm=sha1&q-ak=*************JTUcikdRfpuskSUVd4PZbgd&q-sign-time=1779798367%3B1780403227&q-key-time=1779798367%3B1780403227&q-header-list=host&q-url-param-list=&q-signature=51d24ba6906aa4ff9df4103169e3606d4bc650ef"
                ]
            }
        ],
        "Total": 1,
        "RequestId": "748b8335-f8b3-4eaf-aa67-bc284c4dc45a"
    }
}
```

**Example 2: 查询任务列表接口-按任务类型过滤**

按任务类型过滤

Input: 

```
tccli mps DescribeAigcTaskList --cli-unfold-argument  \
    --QueryTaskFilter.TaskType VideoRedraw
```

Output: 
```
{
    "Response": {
        "PageNum": 1,
        "PageSize": 10,
        "Tasks": [
            {
                "CreateTime": "2026-05-26 20:19:49",
                "FinishedTime": "2026-05-26 20:27:08",
                "RequestBody": "\"{\\\"Input\\\":{\\\"Url\\\":\\\"https://lewis-1302487817.cos.ap-guangzhou.myqcloud.com/replace-test/1s.mp4\\\"},\\\"Action\\\":\\\"CreateVideoRedrawTask\\\",\\\"RequestId\\\":\\\"3a35e21a-f31a-4a49-983f-0b7fc4ab5214\\\",\\\"Uin\\\":\\\"600000563781\\\",\\\"ApiModule\\\":\\\"mps\\\",\\\"Region\\\":\\\"\\\",\\\"AppId\\\":1300057355}\"",
                "ScheduledTime": "2026-05-26 20:19:50",
                "TaskId": "5ddc84c0-fe47-4cc8-35b8-ae8c313d1b9e",
                "TaskStatus": "FINISHED",
                "TaskType": "RedrawVideo",
                "Urls": [
                    "https://aigc-redraw-output-1311402212.cos.ap-guangzhou.myqcloud.com/5ddc84c0-fe47-4cc8-35b8-ae8c313d1b9e/redraw_output.mp4?q-sign-algorithm=****&q-ak=************************skSUVd4PZbgd&q-sign-time=1779798367%3B1780403227&q-key-time=1779798367%3B1780403227&q-header-list=host&q-url-param-list=&q-signature=51d24ba6906aa4ff9df4103169e3606d4bc650ef"
                ]
            }
        ],
        "Total": 22,
        "RequestId": "3328c124-d304-42d2-b926-01adae1c10ee"
    }
}
```

