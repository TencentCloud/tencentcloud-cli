**Example 1: 查询指定实例所属metacluster**



Input: 

```
tccli tcr DescribeMetaClusterId --cli-unfold-argument  \
    --InstanceId tcr-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "MetaClusterId": "cls-xxxxxxxx",
        "RequestId": "a1be36f0-1aa4-4af2-a289-da021bcef89f"
    }
}
```

