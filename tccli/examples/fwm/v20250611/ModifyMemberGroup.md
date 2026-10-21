**Example 1: 设置成员账户组**



Input: 

```
tccli fwm ModifyMemberGroup --cli-unfold-argument  \
    --UserMemberId mem-1300846651-100011616646 \
    --GroupId acg-rwqqudnm
```

Output: 
```
{
    "Response": {
        "RequestId": "a0ba0f23-a0c7-4749-b2b7-936fec906aab"
    }
}
```

**Example 2: 移除账号组成员**



Input: 

```
tccli fwm ModifyMemberGroup --cli-unfold-argument  \
    --UserMemberId mem-1300846651-100011616646
```

Output: 
```
{
    "Response": {
        "RequestId": "086e2336-1a1f-47ad-a919-1b99cf0cbb33"
    }
}
```

