**Example 1: 终端用户绑定设备**



Input: 

```
tccli iotvideo CreateBinding --cli-unfold-argument  \
    --AccessId -9223371585883208722 \
    --Tid ******** \
    --Role owner \
    --ForceBind true
```

Output: 
```
{
    "Response": {
        "AccessToken": "***********",
        "RequestId": "6a04a610-b701-40bf-9a76-f8d5cce01160"
    }
}
```

