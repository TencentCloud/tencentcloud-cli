**Example 1: 查看开机结果**

查看开机结果

Input: 

```
tccli ckafka DescribeRollbackAsyncRequestResult --cli-unfold-argument  \
    --AsyncRequestId abc
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

