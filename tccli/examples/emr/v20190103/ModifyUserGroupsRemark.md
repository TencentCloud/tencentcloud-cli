**Example 1: 修改用户组备注信息**



Input: 

```
tccli emr ModifyUserGroupsRemark --cli-unfold-argument  \
    --InstanceId emr-mzkssfla \
    --GroupNames jianpan-1 \
    --Description 用户组
```

Output: 
```
{
    "Response": {
        "RequestId": "b0c4cfb8-ab11-4819-9219-9909c11df9f8"
    }
}
```

