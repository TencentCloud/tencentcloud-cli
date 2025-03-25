**Example 1: 修改用户Hba**

修改用户Hba

Input: 

```
tccli cdwpg ModifyUserHba --cli-unfold-argument  \
    --InstanceId cdwpg-abcxxxxx \
    --HbaConfigs.0.Type host \
    --HbaConfigs.0.Database all \
    --HbaConfigs.0.User all \
    --HbaConfigs.0.Address 9.0.0.0/24 \
    --HbaConfigs.0.Mask 0 \
    --HbaConfigs.0.Method md5 \
    --HbaConfigs.1.Type host \
    --HbaConfigs.1.Database all \
    --HbaConfigs.1.User all \
    --HbaConfigs.1.Address 0.0.0.0/0 \
    --HbaConfigs.1.Mask  \
    --HbaConfigs.1.Method md5
```

Output: 
```
{
    "Response": {
        "RequestId": "2dd36228-8290-43b7-b83c-ff71cf6f5fd4",
        "TaskId": 9898,
        "ErrorMsg": ""
    }
}
```

