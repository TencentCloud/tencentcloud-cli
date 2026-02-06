**Example 1: 预算提醒记录**

成功示例

Input: 

```
tccli billing DescribeBudgetRemindRecordList --cli-unfold-argument  \
    --PageNo 1 \
    --PageSize 1 \
    --BudgetId 123
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": {
            "CountId": null,
            "Current": 1,
            "MaxLimit": null,
            "OptimizeCountSql": true,
            "Orders": [],
            "Pages": 12,
            "Records": [
                {
                    "AlarmType": "BUDGET",
                    "BudgetQuota": "",
                    "CreateTime": 1640048401000,
                    "DateDesc": "month",
                    "MessageContent": "\r\n预算名称: CVM预算, 预算周期: 月度, 预算类型: 费用预算, 预算金额: 0.0, 提醒类型: 预测金额, 条件: 预算金额的百分比, 阈值: 大于等于10%, 金额: 0元\r\n",
                    "RealCost": "100.00",
                    "SendTime": 1640048400000
                }
            ],
            "SearchCount": true,
            "Size": 1,
            "Total": 12
        },
        "Message": null,
        "RequestId": "b6862d8d-ad0d-488b-9900-e046d3e2a736"
    }
}
```

