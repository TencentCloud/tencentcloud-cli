**Example 1: 示例2**



Input: 

```
tccli cat DescribeProbeTasks --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "81a92494-0fb9-4b10-8ce4-bfa4565cf4eb",
        "TaskSet": null,
        "Total": 0
    }
}
```

**Example 2: 示例3**



Input: 

```
tccli cat DescribeProbeTasks --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "11483de9-9be5-4537-a846-339a57f0e90e",
        "TaskSet": null,
        "Total": 0
    }
}
```

**Example 3: 示例5**



Input: 

```
tccli cat DescribeProbeTasks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "d7628289-fd3c-4acf-a140-a33dd02b3ff6",
        "TaskSet": null,
        "Total": 0
    }
}
```

**Example 4: 查询拨测任务列表**



Input: 

```
tccli cat DescribeProbeTasks --cli-unfold-argument  \
    --TaskIDs task-xx \
    --TagFilters.0.Key name \
    --TagFilters.0.Value zhangsan
```

Output: 
```
{
    "Response": {
        "TaskSet": [
            {
                "Name": "cron测试",
                "TaskId": "task-xx",
                "TaskType": 0,
                "Nodes": [
                    "10000"
                ],
                "NodeIpType": 0,
                "Interval": 0,
                "Parameters": "{\"ipType\":0,\"netIcmpOn\":1,\"netIcmpActivex\":0,\"netIcmpTimeout\":20,\"netIcmpInterval\":\"0.5\",\"netIcmpNum\":4,\"netIcmpSize\":4,\"netIcmpDataCut\":1,\"netDnsOn\":0,\"netTracertOn\":1,\"netTracertTimeout\":20,\"netTracertNum\":0}",
                "Status": 0,
                "TargetAddress": "www.test.com",
                "PayMode": 0,
                "OrderState": 0,
                "TaskCategory": 0,
                "CreatedAt": "2024-01-02 16:57:15",
                "Cron": "* 0-6 * * *",
                "CronState": 0,
                "TagInfoList": [
                    {
                        "Key": "部门",
                        "Value": "部门 1"
                    }
                ]
            }
        ],
        "Total": 0,
        "RequestId": "720b3231-5a85-4f05-aaab-c9b9596xxxxx"
    }
}
```

