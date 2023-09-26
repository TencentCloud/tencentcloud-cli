**Example 1: 添加角色**

添加角色

Input: 

```
tccli trocket CreateRole --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --Role testRole \
    --Remark testRemark \
    --PermWrite True \
    --PermRead True
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "0bb79e96-2531-4088-8d90-e1372c15518a",
        "Role": "testRole"
    }
}
```

