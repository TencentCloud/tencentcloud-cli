**Example 1: DescribeModels**



Input: 

```
tccli hai DescribeModels --cli-unfold-argument  \
    --ModelIds mdl-x39pcr9u
```

Output: 
```
{
    "Response": {
        "ModelSet": [
            {
                "CommunityUrl": "https://cloud.tencent.com/developer/article/2496039",
                "ConfigEnvironment": "CentOS 5.4 64位; nvidia 535.216.01| cuda12.2 | LLM",
                "Description": "模型进行了一个小版本升级，当前版本为 DeepSeek-R1-0528。在最新更新中，DeepSeek R1 通过利用更多的计算资源并在后训练过程中引入算法优化机制，显著提高了其推理和推断能力的深度。该模型在各种基准测试中表现出色，包括数学、编程和一般逻辑方面。其整体性能现已接近领先模型，如 O3 和 Gemini 2.5 Pro。",
                "GuideUrl": "https://cloud.tencent.com/developer/article/2498480",
                "ModelId": "mdl-x39pcr9u",
                "ModelName": "deepseek R1",
                "ModelState": "ONLINE",
                "Tags": [
                    "大语言模型",
                    "文本生成",
                    "NVDIA",
                    "深度求索",
                    "600B以上"
                ]
            }
        ],
        "RequestId": "c6d968d0-9082-44c5-bf39-8726c900d6ea",
        "TotalCount": 1
    }
}
```

