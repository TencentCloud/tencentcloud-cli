**Example 1: 修改环境角色授权**



Input: 

```
tccli tdmq ModifyEnvironmentRole --cli-unfold-argument  \
    --EnvironmentId default \
    --RoleName test_role \
    --Permissions abc \
    --ClusterId pulsar-xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "20846f8d-6438-4cd9-a2a4-09d5f4e8f0db"
    }
}
```

