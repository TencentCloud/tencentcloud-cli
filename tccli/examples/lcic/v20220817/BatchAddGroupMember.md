**Example 1: 批量增加成员到群组**

批量增加成员列表到群组

Input: 

```
tccli lcic BatchAddGroupMember --cli-unfold-argument  \
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

