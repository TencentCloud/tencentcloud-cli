**Example 1: 设置高危命令事件状态**

设置高危命令事件状态

Input: 

```
tccli yunjing SetBashEventsStatus --cli-unfold-argument  \
    --Ids 1 2 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

