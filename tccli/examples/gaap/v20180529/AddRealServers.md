**Example 1: 添加源站**



Input: 

```
tccli gaap AddRealServers --cli-unfold-argument  \
    --ProjectId 0 \
    --RealServerName 'test' \
    --RealServerIP 1.1.1.1
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

**Example 2: AddRealServers**



Input: 

```
tccli gaap AddRealServers --cli-unfold-argument  \
    --ProjectId 0 \
    --RealServerName benny \
    --RealServerIP 106.52.70.76
```

Output: 
```
{
    "Response": {
        "RequestId": "be13ee03-60e8-4af1-880a-e84e5abdf6bc",
        "RealServerSet": [
            {
                "RealServerIP": "106.52.70.76",
                "RealServerId": "rs-hx4u5379"
            }
        ]
    }
}
```

