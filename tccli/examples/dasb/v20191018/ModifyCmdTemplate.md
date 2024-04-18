**Example 1: 修改高危命令模板**

修改高危命令模板

Input: 

```
tccli dasb ModifyCmdTemplate --cli-unfold-argument  \
    --Id 1 \
    --Name 模板a \
    --CmdList cd /root
```

Output: 
```
{
    "Response": {
        "RequestId": "sada123"
    }
}
```

