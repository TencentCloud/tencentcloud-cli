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
        "RequestId": "9a6bd110-20fc-4e08-b78b-a5656cb6151c"
    }
}
```

