**Example 1: 修改复制组信息**

修改复制组信息

Input: 

```
tccli redis ModifyReplicationGroup --cli-unfold-argument  \
    --GroupId crs-rpl-oxsincth \
    --GroupName abc \
    --Remark abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

