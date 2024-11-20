**Example 1: 剔除或切回任务状态查询**

CSM进行节点剔除或者加回时，查看任务是否完成

Input: 

```
tccli trocket DescribeBrokerStatus --cli-unfold-argument  \
    --InstanceId rocket-vip-basic-1 \
    --TaskId 4ed3a07b-36ef-4522-968b-5434dff663da
```

Output: 
```
{
    "Response": {
        "TaskStatus": "Completed",
        "RequestId": "abc"
    }
}
```

