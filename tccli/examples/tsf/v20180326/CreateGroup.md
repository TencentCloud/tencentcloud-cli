**Example 1: 创建虚拟机部署组**



Input: 

```
tccli tsf CreateGroup --cli-unfold-argument  \
    --ApplicationId application-xxxxxxx \
    --GroupName demo \
    --NamespaceId namespace-xxxxxxx \
    --ClusterId cluster-xxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "756cb544-f455-4698-8dfd-feb55d0af366",
        "Result": "group-xxxxxxx"
    }
}
```

