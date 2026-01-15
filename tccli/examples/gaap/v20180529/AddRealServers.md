**Example 1: AddRealServers**



Input: 

```
tccli gaap AddRealServers --cli-unfold-argument  \
    --ProjectId 0 \
    --RealServerIP 22.22.22.23 \
    --RealServerName real-ip-name
```

Output: 
```
{
    "Response": {
        "RealServerSet": [
            {
                "RealServerIP": "22.22.22.23",
                "RealServerId": "rs-9vv3741d"
            }
        ],
        "RequestId": "be58ef1d-25a4-4a71-b33a-9686a1258ae5"
    }
}
```

**Example 2: 添加源站**



Input: 

```
tccli gaap AddRealServers --cli-unfold-argument  \
    --ProjectId 0 \
    --RealServerIP 44.4.4.4 \
    --RealServerName server-name
```

Output: 
```
{
    "Response": {
        "RealServerSet": [
            {
                "RealServerIP": "44.4.4.4",
                "RealServerId": "rs-1008nt4p"
            }
        ],
        "RequestId": "4aaf1f09-5a29-4595-af3f-81cc3098ed3c"
    }
}
```

