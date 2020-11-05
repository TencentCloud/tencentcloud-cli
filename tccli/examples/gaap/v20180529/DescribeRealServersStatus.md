**Example 1: Querying the Binding Status of the Origin Server**

Query the binding status of the origin server.

Input: 

```
tccli gaap DescribeRealServersStatus --cli-unfold-argument  \
    --RealServerIds rs-4ftghy6
```

Output: 
```
{
    "Response": {
        "RealServerStatusSet": [
            {
                "RealServerId": "rs-4ftghy6",
                "BindStatus": 0,
                "ProxyId": "link-asfke"
            }
        ],
        "TotalCount": 1,
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd"
    }
}
```

