**Example 1: 创建电子印章**



Input: 

```
tccli essbasic CreateSeal --cli-unfold-argument  \
    --Caller.ApplicationId c17bdf9c2a7bdcb32611f4d0200fee3d \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId 9990ccd83a8cf53376c557c538f9e9d3 \
    --SealName 图片base64创建印章 \
    --UserId  \
    --Image iVBORw0KGgoAAAANSUhEUgAAADgAAAA4CAYAAACohjseAAABQmlDQ1BJQ0MgUHJvZmlsZQAAKJFjYGASSCwoyGFhYGDIzSspCnJ3UoiIjFtei99Xv7IFe/R9Cv8txOkVQp9PsAChc0pDoBU5CEJB19qhPWOQSOWbJu51U/x/8Ab3gBfya6P8H7c2hqS5ShIQAAAAASUVORK5CYII= \
    --SealType OFFICIAL \
    --SourceIp 123.123.123.123 \
    --FileId  \
    --IsDefault False
```

Output: 
```
{
    "Response": {
        "RequestId": "s1609901021610899889",
        "SealId": "4fecde8c3137d320e8a3c8136bdbb7e5"
    }
}
```

