**Example 1: 获取指定迁移任务详情**

获取指定迁移任务详情

Input: 

```
tccli msp DescribeMigrationTask --cli-unfold-argument  \
    --TaskId msp-1vogxxxx
```

Output: 
```
{
    "Response": {
        "TaskStatus": [
            {
                "Status": "unstart",
                "Progress": "-",
                "UpdateTime": "2018-07-16 17:27:45"
            },
            {
                "Status": "migrating",
                "Progress": "-",
                "UpdateTime": "2018-07-16 17:27:45"
            },
            {
                "Status": "finish",
                "Progress": "-",
                "UpdateTime": "2018-07-16 17:40:51"
            }
        ],
        "RequestId": "ca59d091-0d07-4516-8375-dd88db394b81"
    }
}
```

