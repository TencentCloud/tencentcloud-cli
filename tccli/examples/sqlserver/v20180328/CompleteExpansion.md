**Example 1: 立即完成实例升级**

立即完成实例状态为“升级待切换”的升级操作。

Input: 

```
tccli sqlserver CompleteExpansion --cli-unfold-argument  \
    --InstanceId mssql-2pohwxbf
```

Output: 
```
{
    "Response": {
        "FlowId": 1002591,
        "RequestId": "6353b539-bcd4-41fa-8d6a-98c94601f77d"
    }
}
```

