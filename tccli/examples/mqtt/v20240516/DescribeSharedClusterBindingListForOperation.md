**Example 1: 示例**



Input: 

```
tccli mqtt DescribeSharedClusterBindingListForOperation --cli-unfold-argument  \
    --Uin ******* \
    --InstanceType BASIC
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CdbId": "cdb-3x542xo",
                "ClusterId": "mqtt-broker-cddev-2",
                "CreateTime": 1777453229000,
                "Enabled": true,
                "InstanceType": "BASIC",
                "Remark": "MQTT基础版",
                "Uin": "*******",
                "UpdateTime": 1777453229000
            }
        ],
        "RequestId": "5d45df74-0dca-4faa-aa12-5ae924a251d8"
    }
}
```

