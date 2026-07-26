**Example 1: 批量删除用户**



Input: 

```
tccli tdmysql DeleteUsers --cli-unfold-argument  \
    --InstanceId tdsql3-831053d8 \
    --Users.0.UserName test1 \
    --Users.0.Host %
```

Output: 
```
{
    "Response": {
        "FlowId": 4295045725,
        "RequestId": "ec6aa946-8e1c-4664-a2e4-85fbac308c45"
    }
}
```

