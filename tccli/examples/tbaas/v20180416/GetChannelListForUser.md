**Example 1: GetChannelListForUser**



Input: 

```
tccli tbaas GetChannelListForUser --cli-unfold-argument  \
    --Module channel_mng \
    --Operation channel_list_for_user \
    --ClusterId 251005746envnew \
    --GroupName hellorog \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ChannelList": [
            {
                "ChannelName": "tongdaogz",
                "PeerList": [
                    {
                        "PeerName": "peer0-qtagzorg.bcku93u4ke0g"
                    }
                ]
            }
        ],
        "RequestId": "32439457-7b4b-4b33-94e6-b3dc29a75d31"
    }
}
```

