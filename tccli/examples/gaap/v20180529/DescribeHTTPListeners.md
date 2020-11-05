**Example 1: Querying the HTTP Listener Information**

Query the HTTP listener Information.

Input: 

```
tccli gaap DescribeHTTPListeners --cli-unfold-argument  \
    --ProxyId link-n9ha8jzl\
    --Offset 0\
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 4,
        "ListenerSet": [
            {
                "Protocol": "HTTP",
                "ListenerId": "listener-4e99n24b",
                "Port": 80,
                "ListenerStatus": 0,
                "ListenerName": "http80",
                "CreateTime": 1563335063
            },
            {
                "Protocol": "HTTP",
                "ListenerId": "listener-jmi21mrf",
                "Port": 8080,
                "ListenerStatus": 0,
                "ListenerName": "http8080",
                "CreateTime": 1564590945
            },
            {
                "Protocol": "HTTP",
                "ListenerId": "listener-1grazsz5",
                "Port": 18080,
                "ListenerStatus": 0,
                "ListenerName": "http18080",
                "CreateTime": 1564590963
            },
            {
                "Protocol": "HTTP",
                "ListenerId": "listener-l6z66uqb",
                "Port": 28080,
                "ListenerStatus": 0,
                "ListenerName": "http28080",
                "CreateTime": 1564640821
            }
        ],
        "RequestId": "4c43a7f7-3527-4e2a-9998-bbd363e4b095"
    }
}
```

