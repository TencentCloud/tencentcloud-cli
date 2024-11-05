**Example 1: 修改反弹shell事件状态**



Input: 

```
tccli tcss ModifyReverseShellStatus --cli-unfold-argument  \
    --EventIdSet "365456" \
    --Status EVENT_DEALED \
    --Remark "删除原因"
```

Output: 
```
{
    "Response": {
        "RequestId": "15cf63db-11a9-4885-b1a3-211dd54b83b7"
    }
}
```

