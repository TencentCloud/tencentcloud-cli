**Example 1: 启动一个订阅任务的校验**

启动一个订阅任务的校验。任务必须已经成功调用ConfigureSubscribe接口配置了所有的必要信息才能启动校验。

Input: 

```
tccli dts CreateSubscribeCheckJob --cli-unfold-argument  \
    --SubscribeId subs-l4d3a7izai
```

Output: 
```
{
    "Response": {
        "RequestId": "77501ba0-f097-11ed-ac7d-b1056735c0c8"
    }
}
```

