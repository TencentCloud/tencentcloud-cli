**Example 1: 添加源站**



Input: 

```
tccli gaap AddRealServers --cli-unfold-argument  \
    --ProjectId 0\
    --RealServerIP 1.1.1.1\
    --RealServerName 'test'
```

Output: 
```
{
    "Response": {
        "RealServerSet": [
            {
                "RealServerId": "id-5dr8gu4",
                "RealServerIP": "1.1.1.1"
            }
        ],
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd"
    }
}
```

