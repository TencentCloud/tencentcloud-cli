**Example 1: DescribeSystemVariableList**



Input: 

```
tccli adp DescribeSystemVariableList --cli-unfold-argument  \
    --AppId 206***********85184
```

Output: 
```
{
    "Response": {
        "SystemVariableList": [
            {
                "Description": "本轮对话内容",
                "Name": "SYS.UserQuery"
            }
        ],
        "RequestId": "9a337709-a67a-4d9f-a484-8450c5608b30"
    }
}
```

