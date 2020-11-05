**Example 1: Querying the Information of Listeners and Connections from Which the Statistics Can Be Derived**

Query the information of listeners and connections from which the statistics can be derived.

Input: 

```
tccli gaap DescribeProxyAndStatisticsListeners --cli-unfold-argument  \
    --ProjectId 0
```

Output: 
```
{
    "Response": {
        "ProxySet": [
            {
                "ProxyId": "link-mmu241ob",
                "PorxyName": "wegame",
                "ListenerList": [
                    {
                        "ListenerId": "listener-lmifrrmh",
                        "ListenerName": "wegame",
                        "Protocol": "HTTP",
                        "Port": 80
                    }
                ]
            }
        ],
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd",
        "TotalCount": 1
    }
}
```

