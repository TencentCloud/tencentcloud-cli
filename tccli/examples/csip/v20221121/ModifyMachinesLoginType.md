**Example 1: 关闭扫码登录**

关闭扫码登录

Input: 

```
tccli csip ModifyMachinesLoginType --cli-unfold-argument  \
    --LoginType 0 \
    --Scope 1 \
    --From 1 \
    --RequestVersion 1
```

Output: 
```
{
    "Response": {
        "RequestId": "ad9c4066-5339-4a6d-a42c-498afa737347",
        "TaskId": 11919
    }
}
```

**Example 2: 成功**



Input: 

```
tccli csip ModifyMachinesLoginType --cli-unfold-argument  \
    --LoginType 1 \
    --InstanceIds ins-jadv34x ins-kv34ivm
```

Output: 
```
{
    "Response": {
        "TaskId": 1,
        "RequestId": "d16a1915-09af-4153-8a73-9e5a8d9f6407"
    }
}
```

