**Example 1: 终端用户临时访问设备授权**



Input: 

```
tccli iotvideo CreateDevToken --cli-unfold-argument  \
    --AccessId ******** \
    --TtlMinutes 10 \
    --Tids ********
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AccessId": "********",
                "Tid": "********",
                "AccessToken": "********",
                "ExpireTime": 1583740326
            }
        ],
        "RequestId": "fed147b1-5b54-4589-b502-60f3dbfe2478"
    }
}
```

