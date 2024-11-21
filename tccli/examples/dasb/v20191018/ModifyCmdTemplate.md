**Example 1: 修改高危命令模板**

修改高危命令模板

Input: 

```
tccli dasb ModifyCmdTemplate --cli-unfold-argument  \
    --Id 1 \
    --Name 高危命令模板 \
    --CmdList rm -rf
```

Output: 
```
{
    "Response": {
        "RequestId": "dfac9070-8b23-499e-83b2-a50e3ca059af"
    }
}
```

