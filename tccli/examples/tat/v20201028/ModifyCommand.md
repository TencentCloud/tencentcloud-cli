**Example 1: 修改命令**



Input: 

```
tccli tat ModifyCommand --cli-unfold-argument  \
    --CommandName second-command \
    --Description hello world! \
    --Content cHM= \
    --CommandType SHELL \
    --WorkingDirectory / \
    --Timeout 600 \
    --CommandId cmd-63usjhmq
```

Output: 
```
{
    "Response": {
        "RequestId": "9bea970a-0bab-495f-b0dd-de5eedfdf611"
    }
}
```

