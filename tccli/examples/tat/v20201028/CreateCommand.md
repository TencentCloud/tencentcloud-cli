**Example 1: 创建命令**



Input: 

```
tccli tat CreateCommand --cli-unfold-argument  \
    --CommandName hello-command \
    --Description hello world \
    --Content bHM= \
    --CommandType SHELL \
    --WorkingDirectory / \
    --Timeout 60
```

Output: 
```
{
    "Response": {
        "RequestId": "9bea970a-0bab-495f-b0dd-de5eedfdf611",
        "CommandId": "cmd-7efujjs6"
    }
}
```

