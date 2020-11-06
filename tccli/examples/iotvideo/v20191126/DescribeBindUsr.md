**Example 1: 查询设备绑定的终端用户列表**



Input: 

```
tccli iotvideo DescribeBindUsr --cli-unfold-argument  \
    --AccessId -9223371585883208724 \
    --Tid ************
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AccessId": "-9223371585883208724",
                "Role": "owner"
            }
        ],
        "RequestId": "edb26918-e167-4eaa-ac7a-401b010f54a7"
    }
}
```

