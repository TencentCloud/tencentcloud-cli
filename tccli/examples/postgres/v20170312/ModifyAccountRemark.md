**Example 1: Modifying account remarks**



Input: 

```
tccli postgres ModifyAccountRemark --cli-unfold-argument  \
    --DBInstanceId postgres-6bwgamo3 \
    --UserName test \
    --Remark testModifyRemark
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

