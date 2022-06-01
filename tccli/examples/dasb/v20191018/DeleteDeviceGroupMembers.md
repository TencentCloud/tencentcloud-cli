**Example 1: 删除资产组成员**

删除资产组成员

Input: 

```
tccli dasb DeleteDeviceGroupMembers --cli-unfold-argument  \
    --Id 1 \
    --MemberIdSet 1 2 3
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

