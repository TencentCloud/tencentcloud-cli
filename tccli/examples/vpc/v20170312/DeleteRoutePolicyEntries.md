**Example 1: 删除路由接收策略条目**

删除路由接收策略条目。

Input: 

```
tccli vpc DeleteRoutePolicyEntries --cli-unfold-argument  \
    --RoutePolicyId rrp-azd4dt1c \
    --RoutePolicyEntrySet.0.RoutePolicyEntryId rrpi-la0vk0g3
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

