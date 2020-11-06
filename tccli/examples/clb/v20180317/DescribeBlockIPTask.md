**Example 1: 查询封禁IP（黑名单）异步任务的执行状态**



Input: 

```
tccli clb DescribeBlockIPTask --cli-unfold-argument  \
    --TaskId localjob010916173469001234567890
```

Output: 
```
{
    "Response": {
        "Status": 6,
        "RequestId": "83329908-a282-4f9f-8ab-033a3025baff"
    }
}
```

