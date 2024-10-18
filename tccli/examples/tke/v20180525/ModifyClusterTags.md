**Example 1: 修改集群标签**

修改集群标签

Input: 

```
tccli tke ModifyClusterTags --cli-unfold-argument  \
    --ClusterId cls-0gudq56e \
    --Tags.0.Key abc \
    --Tags.0.Value abc \
    --SyncSubresource True
```

Output: 
```
{
    "Response": {
        "Tags": [
            {
                "Key": "abc",
                "Value": "abc"
            }
        ],
        "RequestId": "33483fde-efec-4d3c-8ff6-340d9dbc2d01"
    }
}
```

