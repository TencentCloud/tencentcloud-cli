**Example 1: 创建一个虚拟分组**



Input: 

```
tccli ioa CreateAccountVirtualGroup --cli-unfold-argument  \
    --VirtualGroupName 研发三组 \
    --AccountGroupId 3338 \
    --DomainInstanceId 1 \
    --Description 研发三组
```

Output: 
```
{
    "Response": {
        "Data": {
            "VirtualGroupId": 167
        },
        "RequestId": "3ea29182-75a6-4752-b507-04ed7dca7e52"
    }
}
```

