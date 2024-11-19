**Example 1: 修改复制组信息**

修改复制组信息

Input: 

```
tccli redis ModifyReplicationGroup --cli-unfold-argument  \
    --GroupId crs-rpl-oxsincth \
    --GroupName group-name-1 \
    --Remark note-XXX
```

Output: 
```
{
    "Response": {
        "RequestId": "b778637c-1c49-46a5-b958-64b6caXXXXXX"
    }
}
```

