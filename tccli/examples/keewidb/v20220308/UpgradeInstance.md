**Example 1: 扩分片数示例**

扩容实例内存容量、分片数量以及磁盘容量。

Input: 

```
tccli keewidb UpgradeInstance --cli-unfold-argument  \
    --ShardNum 6 \
    --InstanceId kee-lagg****
```

Output: 
```
{
    "Response": {
        "DealId": "1655902380",
        "RequestId": "12eb8b4f-8aab-43df-aea4-d4192e18eac7"
    }
}
```

