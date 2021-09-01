**Example 1: 修改脚本**



Input: 

```
tccli bm ModifyUserCmd --cli-unfold-argument  \
    --CmdId cmd-xxxxx \
    --Alias 新名字 \
    --OsType linux \
    --Content test
```

Output: 
```
{
    "Response": {
        "RequestId": "d432b25f-6878-4d1d-865e-34bd040122e9"
    }
}
```

