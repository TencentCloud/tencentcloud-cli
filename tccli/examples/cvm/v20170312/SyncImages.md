**Example 1: Syncing an image**

This example shows you how to sync an image `img-o3ycss2p` to the Guangzhou region.

Input: 

```
tccli cvm SyncImages --cli-unfold-argument  \
    --ImageIds img-o3ycss2p\
    --DestinationRegions ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
    }
}
```

