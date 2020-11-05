**Example 1: Querying the Information of Connections and Connection Groups from Which the Statistics Can Be Derived**

Query the information of connections and connection groups from which the statistics can be derived.

Input: 

```
tccli gaap DescribeGroupAndStatisticsProxy --cli-unfold-argument  \
    --ProjectId 0
```

Output: 
```
{
    "Response": {
        "GroupSet": [
            {
                "GroupId": "lg-r737geg",
                "GroupName": "lg-test",
                "ProxySet": [
                    {
                        "ProxyId": "link-mmu241ob",
                        "PorxyName": "link-test",
                        "ListenerList": [
                            {
                                "ListenerId": "listener-lmifrrmh",
                                "ListenerName": "linstener-test",
                                "Port": 80,
                                "Protocol": "HTTP"
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd",
        "TotalCount": 1
    }
}
```

