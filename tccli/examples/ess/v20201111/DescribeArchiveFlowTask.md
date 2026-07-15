**Example 1: 根据任务id查询归档任务状态**



Input: 

```
tccli ess DescribeArchiveFlowTask --cli-unfold-argument  \
    --Operator.UserId yDtT9UUck*****************NQ0bO6 \
    --TaskId yD3h6UUck*****************bBSBfp
```

Output: 
```
{
    "Response": {
        "ArchiveFlowResults": [
            {
                "ArchiveFlowStatus": 0,
                "BusinessId": "测试1-business_id",
                "ErrorMessage": "",
                "FlowId": "yD3h6UUckp***************2sDw4ME",
                "ResourceIdList": [
                    "yD3hnUUck*****************OnrcHE"
                ]
            }
        ],
        "Status": 2,
        "RequestId": "45ba5969-15db-407b-8eb7-454884394151"
    }
}
```

