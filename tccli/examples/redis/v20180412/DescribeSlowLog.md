**Example 1: 请求示例**



Input: 

```
tccli redis DescribeSlowLog --cli-unfold-argument  \
    --InstanceId crs-asdasdas \
    --EndTime 2019-09-09 12:12:41 \
    --BeginTime 2019-09-08 12:12:41
```

Output: 
```
{
    "Response": {
        "InstanceSlowlogDetail": [
            {
                "Node": "833a2f6d8b402319aee8ad7f1c0fbbf7a6604337",
                "Command": "hget",
                "CommandLine": "hget hash_key classify_scope::default",
                "Duration": 45,
                "ExecuteTime": "2019-09-08 12:13:08",
                "Client": ""
            },
            {
                "Node": "833a2f6d8b402319aee8ad7f1c0fbbf7a6604337",
                "Command": "keys",
                "CommandLine": "keys OtherResControler:orion.ovs.client.1514259512471:orion.ovs.entprise.9281083591:sence:*",
                "Duration": 41,
                "ExecuteTime": "2019-09-08 12:13:08",
                "Client": ""
            },
            {
                "Node": "24a05f0d545da235f07a5bc5deebb937af8f721e",
                "Command": "get",
                "CommandLine": "get slot::fsm::status::orion.ovs.client.1508751991541::1db7ffcf9216bc1fd939e6c710514f6fb40fd4fe1525f",
                "Duration": 41,
                "ExecuteTime": "2019-09-08 12:13:08",
                "Client": ""
            }
        ],
        "RequestId": "121d5b40-d2b8-11e9-8c40-ef686158cbd6",
        "TotalCount": 106980
    }
}
```

