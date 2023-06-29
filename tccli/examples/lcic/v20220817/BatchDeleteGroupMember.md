**Example 1: 批量删除成员从群组列表**

批量删除成员从群组列表

Input: 

```
tccli lcic BatchDeleteGroupMember --cli-unfold-argument  \
    --GroupIds abcdfdfg dfgsdgsdg \
    --SdkAppId 12345678 \
    --MemberIds dfgdfg
```

Output: 
```
{
    "Response": {
        "RequestId": "213das"
    }
}
```

