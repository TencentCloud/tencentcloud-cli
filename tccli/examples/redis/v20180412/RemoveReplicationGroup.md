**Example 1: 删除复制组**

当复制组内没有实例时，删除复制组

Input: 

```
tccli redis RemoveReplicationGroup --cli-unfold-argument  \
    --GroupId crs-rpl-oxsincthdd
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

