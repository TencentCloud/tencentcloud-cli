**Example 1: 查看关机结果**

RequestPassword

Input: 

```
tccli ckafka DescribeAttackAsyncRequestResult --cli-unfold-argument  \
    --AsyncRequestId abc \
    --RequestPassword abc
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

