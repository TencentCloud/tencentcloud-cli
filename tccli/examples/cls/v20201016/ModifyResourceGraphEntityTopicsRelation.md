**Example 1: 手动关联实体与topic映射**



Input: 

```
tccli cls ModifyResourceGraphEntityTopicsRelation --cli-unfold-argument  \
    --ResourceGraphId badc7d81-70a6-4979-aa54-59ae51a4870a \
    --EntityId 6e465db7baf3477ae75a7efb5d0d64c7 \
    --TopicInfos.0.TopicId 92005fca-cbf5-45e9-8c55-a506d8ff7238 \
    --TopicInfos.0.Region ap-guangzhou \
    --TopicInfos.0.LogType bussinesslog \
    --TopicInfos.0.BizType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "16d9875b-64bc-4d6c-b290-01b4a7111bcb"
    }
}
```

