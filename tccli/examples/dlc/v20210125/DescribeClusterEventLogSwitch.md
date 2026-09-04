**Example 1: 已开启事件日志**

已开启事件日志分支

Input: 

```
tccli dlc DescribeClusterEventLogSwitch --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "ClusterId": "cls-xxxxxxxx",
        "Enable": true,
        "LogsetId": "d12706e7-ae3b-42cf-9dab-d41e71482193",
        "TopicId": "ec5a1f8e-5234-419b-bf10-e5789e325bdf",
        "TopicRegion": "ap-chengdu",
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

**Example 2: 未开启事件日志**

未开启事件日志分支

Input: 

```
tccli dlc DescribeClusterEventLogSwitch --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "ClusterId": "cls-xxxxxxxx",
        "Enable": false,
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

