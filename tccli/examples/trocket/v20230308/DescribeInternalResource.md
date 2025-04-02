**Example 1: 查询4.x物理集群资源**



Input: 

```
tccli trocket DescribeInternalResource --cli-unfold-argument  \
    --ClusterId rocketmq-dev-02
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "1cd077ae-14ad-40a6-afc4-b7341413f6c0",
        "Token": "ZlaxlrZ",
        "Url": "1.141.103.22:9876"
    }
}
```

