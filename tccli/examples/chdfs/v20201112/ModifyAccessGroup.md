**Example 1: 修改权限组属性**

修改权限组属性

Input: 

```
tccli chdfs ModifyAccessGroup --cli-unfold-argument  \
    --AccessGroupId ag-f8xoises \
    --AccessGroupName access-group-test \
    --Description group-example
```

Output: 
```
{
    "Response": {
        "RequestId": "c77b62ec-b019-46fe-80e9-c842785cf9dc"
    }
}
```

