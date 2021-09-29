**Example 1: 解绑用户上的用户组**



Input: 

```
tccli dlc UnbindWorkGroupsFromUser --cli-unfold-argument  \
    --AddInfo.UserId 1000323 \
    --AddInfo.WorkGroupIds 112
```

Output: 
```
{
    "Response": {
        "RequestId": "edb8ceac-68c9-4acf-9a38-ea26abc61dfc"
    }
}
```

