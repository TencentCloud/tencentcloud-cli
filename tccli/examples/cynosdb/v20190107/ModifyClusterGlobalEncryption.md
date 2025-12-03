**Example 1: 关闭全局加密**



Input: 

```
tccli cynosdb ModifyClusterGlobalEncryption --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xxxxxxxx \
    --IsOpenGlobalEncryption False
```

Output: 
```
{
    "Response": {
        "RequestId": "22f221ae-40d7-4b73-84bb-ae2d090a3beb",
        "TaskId": 177736
    }
}
```

