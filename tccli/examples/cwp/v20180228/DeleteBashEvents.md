**Example 1: 删除高危命令事件**

删除高危命令事件

Input: 

```
tccli cwp DeleteBashEvents --cli-unfold-argument  \
    --Ids 1002 \
    --All True
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

