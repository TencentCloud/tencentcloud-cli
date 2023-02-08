**Example 1: 查询异步任务执行结果**



Input: 

```
tccli vpc DescribeVpcTaskResult --cli-unfold-argument  \
    --TaskId 481e9b6e-81d1-4859-b8cf-a673e010b388
```

Output: 
```
{
    "Response": {
        "Status": "SUCCESS",
        "Output": "SUCCESS",
        "Result": [
            {
                "ResourceId": "eni-olifj433",
                "Status": "SUCCESS"
            }
        ],
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

