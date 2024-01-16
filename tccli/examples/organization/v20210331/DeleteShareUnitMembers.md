**Example 1: 删除共享单元成员**



Input: 

```
tccli organization DeleteShareUnitMembers --cli-unfold-argument  \
    --UnitId shareUnit-xhre**ra2p \
    --Area ap-guangzhou \
    --Members.0.ShareMemberUin 333333333333
```

Output: 
```
{
    "Response": {
        "RequestId": "5ef007aa-2dc5-4729-a880-b7ac69d94714"
    }
}
```

