**Example 1: 查询异步任务状态**

假设某次调用创建转发规则接口返回成功，且返回的 RequestId 为 55c85074-3e7f-4c6d-864f-673660d4f8de，则需要查询该异步任务最终是否执行成功。响应中，Status 为 0 表示任务执行成功。

Input: 

```
tccli clb DescribeTaskStatus --cli-unfold-argument  \
    --TaskId 55c85074-3e7f-4c6d-864f-673660d4f8de
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "LoadBalancerIds": [
            "lb-6efswuxa"
        ],
        "RequestId": "917384bc-5b8d-4b68-a0bc-a58f815e8e3b"
    }
}
```

