**Example 1: 修改角色**

修改角色成功

Input: 

```
tccli trocket ModifyRole --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --Role test_role_name \
    --Remark 测试修改 \
    --PermRead False \
    --PermWrite False
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "0608515b-cde2-41d6-933c-169d0d1849c5"
    }
}
```

