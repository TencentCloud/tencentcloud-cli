**Example 1: 创建用户自定义函数**



Input: 

```
tccli wedata CreateCustomFunction --cli-unfold-argument  \
    --ProjectId abc \
    --Type HIVE \
    --Kind ANALYSIS \
    --ClusterIdentifier abc \
    --DbName abc \
    --Name abc
```

Output: 
```
{
    "Response": {
        "ErrorMessage": "abc",
        "FunctionId": "abc",
        "RequestId": "abc"
    }
}
```

