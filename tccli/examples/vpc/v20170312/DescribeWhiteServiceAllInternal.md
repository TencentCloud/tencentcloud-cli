**Example 1: 用于获取全量的公共服务白名单路由信息**

用于获取全量的公共服务白名单路由信息。

Input: 

```
tccli vpc DescribeWhiteServiceAllInternal --cli-unfold-argument  \
    --WhiteServiceId 123 \
    --Protocol tcp \
    --Vip 1.1.1.1 \
    --VirtualPort 80 \
    --Limit 100 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

