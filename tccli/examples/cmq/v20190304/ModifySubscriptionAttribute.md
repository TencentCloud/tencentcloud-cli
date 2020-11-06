**Example 1: 修改订阅属性**

修改订阅属性

Input: 

```
tccli cmq ModifySubscriptionAttribute --cli-unfold-argument  \
    --TopicName test \
    --SubscriptionName test \
    --BindingKey test
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

