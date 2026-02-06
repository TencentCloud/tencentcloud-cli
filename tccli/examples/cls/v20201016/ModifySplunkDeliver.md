**Example 1: 修改Splun投递任务**



Input: 

```
tccli cls ModifySplunkDeliver --cli-unfold-argument  \
    --TaskId 65a07eec-96ee-458d-850b-53dfe9b43125 \
    --TopicId d1d7d473-827e-4dad-9a42-f0287ad43125 \
    --MetadataInfo.Format json \
    --MetadataInfo.MetaFields __SOURCE__
```

Output: 
```
{
    "Response": {
        "RequestId": "89b26245-ec3e-4b00-829a-bcc835d43125"
    }
}
```

