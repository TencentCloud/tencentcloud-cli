**Example 1: 创建知识库**

创建知识库

Input: 

```
tccli adp CreateKB --cli-unfold-argument  \
    --KbType 2 \
    --SharedSubType 1 \
    --SpaceId default_space \
    --Spec.Name 共享知识库_生效范围综合查询_adp_qta_YFTOka \
    --Spec.Description 标准模式共享知识库测试
```

Output: 
```
{
    "Response": {
        "KbId": "2097704030430616192",
        "RequestId": "d162e414-3a60-45e5-bf87-a8fb10019f4b"
    }
}
```

