**Example 1: 新建高危命令模板**

控制台页面新增高危命令模版

Input: 

```
tccli dasb CreateCmdTemplate --cli-unfold-argument  \
    --Name 高危模版1 \
    --CmdList rm -rf /*
```

Output: 
```
{
    "Response": {
        "Id": 1,
        "RequestId": "as1212j"
    }
}
```

