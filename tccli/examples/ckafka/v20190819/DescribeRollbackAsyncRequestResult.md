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
        "RequestId": "dda6e5eb-eefa-41c9-9ee5-d92942a2987a"
    }
}
```

