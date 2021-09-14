**Example 1: 域名开启中国境内加速。**



Input: 

```
tccli vod ModifyVodDomainAccelerateConfig --cli-unfold-argument  \
    --Domain myexample.com \
    --Area 'Chinese Mainland' \
    --Status Enabled
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4551-9d4b-5594145287e1"
    }
}
```

