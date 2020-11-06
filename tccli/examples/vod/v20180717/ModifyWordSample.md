**Example 1: Modifying keyword sample**



Input: 

```
tccli vod ModifyWordSample --cli-unfold-argument  \
    --Keyword Combat \
    --Usages Review \
    --TagOperationInfo.Type reset \
    --TagOperation.Tags Terrorism
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

