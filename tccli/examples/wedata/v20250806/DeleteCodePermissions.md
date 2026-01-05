**Example 1: 删除文件权限**



Input: 

```
tccli wedata DeleteCodePermissions --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
    --RecyclePolicySet.0.Resource.ResourceType script \
    --RecyclePolicySet.0.Resource.ResourceId fcec3d4e-e099-4c26-9154-0745ee1a9895 \
    --RecyclePolicySet.0.Resource.ResourceIdForPath /cc1c8732-d398-43f8-b5cf-6e66b8258208/fcec3d4e-e099-4c26-9154-0745ee1a9895 \
    --RecyclePolicySet.0.RecycleSubjects.0.SubjectType user \
    --RecyclePolicySet.0.RecycleSubjects.0.SubjectValues 100044085874 \
    --RecyclePolicySet.0.RecycleSubjects.0.Privileges CAN_MANAGE
```

Output: 
```
{
    "Response": {
        "Data": [],
        "RequestId": "34fcc2c3-6a9d-49cd-8411-7bc4e11937be"
    }
}
```

