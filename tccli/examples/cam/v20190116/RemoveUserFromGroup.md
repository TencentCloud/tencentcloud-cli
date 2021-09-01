**Example 1: 从用户组删除用户**



Input: 

```
tccli cam RemoveUserFromGroup --cli-unfold-argument  \
    --Info.0.Uid 1001408 \
    --Info.0.GroupId 2020
```

Output: 
```
{
    "Response": {
        "RequestId": "1fadd33e-6f57-4404-a912-bc00680b89d2"
    }
}
```

