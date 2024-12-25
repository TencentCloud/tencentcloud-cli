**Example 1: 修改实例密码复杂度**



Input: 

```
tccli cdb ModifyInstancePasswordComplexity --cli-unfold-argument  \
    --InstanceIds cdb-93hvf1d \
    --ParamList.0.Name validate_password.length \
    --ParamList.0.CurrentValue 10
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "988d3e5b-4cc7bac7-b92977cf-274603c0",
        "RequestId": "11fa4b07-11b0-4c48-a472-2d835d9bf165"
    }
}
```

