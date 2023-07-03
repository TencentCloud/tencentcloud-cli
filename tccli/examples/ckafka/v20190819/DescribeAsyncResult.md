**Example 1: 查询混沌演练任务执行结果**

RequestPassword

Input: 

```
tccli ckafka DescribeAsyncResult --cli-unfold-argument  \
    --AsyncRequestId abc \
    --RequestPassword abc
```

Output: 
```
{
    "Response": {
        "Code": 1,
        "Msg": "abc",
        "RequestId": "abc"
    }
}
```

