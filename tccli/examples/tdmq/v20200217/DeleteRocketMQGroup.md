**Example 1: 删除订阅组**

https://tdmq.tencentcloudapi.com/?
Action=DeleteRocketMQGroup
&ClusterId=
&NamespaceId=example
&GroupId=group-example
&<公共请求参数>

Input: 

```
tccli tdmq DeleteRocketMQGroup --cli-unfold-argument  \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --NamespaceId test_namespace \
    --GroupId test_group
```

Output: 
```
{
    "Response": {
        "RequestId": "7fb7d925-a5c7-4b8c-add5-8477917a6260"
    }
}
```

