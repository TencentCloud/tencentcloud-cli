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

**Example 2: 修改Splun投递任务-跨账户投递任务**



Input: 

```
tccli cls ModifySplunkDeliver --cli-unfold-argument  \
    --TaskId 565a2f82-22d3-4f2e-b417-0e251805c63a \
    --TopicId 6b81282d-f355-404f-ae1f-6e00b27dfc70 \
    --ExternalRole.RoleArn qcs::cam::uin/1000011275:roleName/splunk \
    --ExternalRole.ExternalId splunk
```

Output: 
```
{
    "Response": {
        "RequestId": "7f4f486d-00f6-4cad-b212-37b789d78d45"
    }
}
```

