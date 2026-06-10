**Example 1: 扩容实例**

扩容实例

Input: 

```
tccli cfw ExpandCfwVertical --cli-unfold-argument  \
    --FwType nat \
    --Width 121 \
    --CfwInstance cfwnat-e366d270 \
    --ElasticSwitch 1 \
    --ElasticBandwidth 290 \
    --Tags.0.TagKey None \
    --Tags.0.TagValue None \
    --ElasticTrafficSwitch 0
```

Output: 
```
{
    "Response": {
        "RequestId": "8fcb913a-80ee-4ace-bf11-7c5a0592be7e"
    }
}
```

