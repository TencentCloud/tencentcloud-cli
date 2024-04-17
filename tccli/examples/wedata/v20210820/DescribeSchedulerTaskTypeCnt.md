**Example 1: 运维大屏-任务状态分布示例**

运维大屏-任务状态分布

Input: 

```
tccli wedata DescribeSchedulerTaskTypeCnt --cli-unfold-argument  \
    --ProjectId 15316096965952 \
    --InCharge allenbguo
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Number": null,
                "TaskType": "26",
                "TypeName": "离线同步"
            },
            {
                "Number": null,
                "TaskType": "34",
                "TypeName": "Hive SQL"
            },
            {
                "Number": null,
                "TaskType": "35",
                "TypeName": "Shell"
            }
        ],
        "RequestId": "742ab36d-d56c-457e-b42a-b721d2a6b091"
    }
}
```

