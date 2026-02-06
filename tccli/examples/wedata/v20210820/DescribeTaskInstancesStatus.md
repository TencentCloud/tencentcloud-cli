**Example 1: 获取运行状态**

获取运行状态

Input: 

```
tccli wedata DescribeTaskInstancesStatus --cli-unfold-argument  \
    --RecordIdList 10505 \
    --WorkflowId a6557acf-1dc4-4251-84c2-c1210d5a6390 \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Instances": [
                    {
                        "InstanceId": "6820250728160909016_2025-07-28T16:09:07+08:00",
                        "RecordId": "10505",
                        "Status": "SUCCESS",
                        "TaskId": "20250728154317627"
                    }
                ]
            }
        ],
        "RequestId": "d3da9408-65b5-4229-9ddf-070ad3cbc2ba"
    }
}
```

