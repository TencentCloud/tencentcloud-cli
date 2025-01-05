**Example 1: 修改集群标签**

修改集群标签

Input: 

```
tccli tke ModifyClusterTags --cli-unfold-argument  \
    --ClusterId cls-0gudq56e \
    --Tags.0.Key product \
    --Tags.0.Value tke \
    --SyncSubresource True
```

Output: 
```
{
    "Response": {
        "Tags": [
            {
                "Key": "product",
                "Value": "tke"
            }
        ],
        "RequestId": "33483fde-efec-4d3c-8ff6-340d9dbc2d01"
    }
}
```

