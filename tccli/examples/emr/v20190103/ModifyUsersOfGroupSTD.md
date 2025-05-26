**Example 1: 修改用户组内用户**



Input: 

```
tccli emr ModifyUsersOfGroupSTD --cli-unfold-argument  \
    --InstanceId emr-o88f3whr \
    --Group group3 \
    --Users user1 \
    --Description modify
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "554a474b-c1dd-4627-9b80-42b4b9e95add"
    }
}
```

