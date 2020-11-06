**Example 1: Sample request**



Input: 

```
tccli redis DescribeProxySlowLog --cli-unfold-argument  \
    --InstanceId crs-asdasdas \
    --BeginTime 2019-09-0812:12:41 \
    --EndTime 2019-09-0912:12:41
```

Output: 
```
{
    "Response": {
        "InstanceProxySlowlogDetail": [
            {
                "Client": "172.16.21.78",
                "Command": "hget",
                "CommandLine": "hget hash_key classify_scope::default",
                "Duration": 45,
                "ExecuteTime": "2019-09-08 12:13:08"
            },
            {
                "Client": "172.16.21.53",
                "Command": "keys",
                "CommandLine": "keys OtherResControler:orion.ovs.client.1514259512471:orion.ovs.entprise.9281083591:sence:*",
                "Duration": 41,
                "ExecuteTime": "2019-09-08 12:13:08"
            },
            {
                "Client": "172.16.31.239",
                "Command": "get",
                "CommandLine": "get slot::fsm::status::orion.ovs.client.1508751991541::1db7ffcf9216bc1fd939e6c710514f6fb40fd4fe1525f",
                "Duration": 41,
                "ExecuteTime": "2019-09-08 12:13:08"
            }
        ],
        "RequestId": "121d5b40-d2b8-11e9-8c40-ef686158cbd6",
        "TotalCount": 106980
    }
}
```

