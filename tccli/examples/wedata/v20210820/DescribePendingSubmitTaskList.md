**Example 1: 获取待提交任务预提交校验信息**

获取待提交任务预提交校验信息

Input: 

```
tccli wedata DescribePendingSubmitTaskList --cli-unfold-argument  \
    --ProjectId abc \
    --WorkflowId abc \
    --TaskIdList abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TaskId": "abc",
                "TaskName": "abc",
                "ModifyType": "abc",
                "TaskStatus": "abc",
                "SubmitPreCheck": "abc",
                "SubmitPreCheckDetailList": [
                    {
                        "TaskId": "abc",
                        "TaskName": "abc",
                        "ProjectId": "abc",
                        "ProjectName": "abc",
                        "InChargeId": "abc",
                        "InCharge": "abc"
                    }
                ],
                "ExecutorGroupId": "abc",
                "ExecutorGroupName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

