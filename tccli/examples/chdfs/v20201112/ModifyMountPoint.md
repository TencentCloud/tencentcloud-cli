**Example 1: 修改挂载点属性**

修改挂载点属性

Input: 

```
tccli chdfs ModifyMountPoint --cli-unfold-argument  \
    --MountPointId f4mnvilzmdd-Tx5f \
    --MountPointName test \
    --MountPointStatus 2
```

Output: 
```
{
    "Response": {
        "RequestId": "7de3434f-ad14-403b-8138-7396549d4bc1"
    }
}
```

