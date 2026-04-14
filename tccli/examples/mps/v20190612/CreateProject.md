**Example 1: 剧集项目创建**



Input: 

```
tccli mps CreateProject --cli-unfold-argument  \
    --ProjectName 斗破苍穹 \
    --TermBase.0.Src Canaan Academy \
    --TermBase.0.Dst 迦南学院 \
    --Description 玄幻题材有声剧 \
    --Speakers.0.SpeakerId xiao_yan \
    --Speakers.0.VoiceId voice_001 \
    --Speakers.0.Gender male \
    --Speakers.0.AgeGroup youth \
    --Speakers.0.Description 主角萧炎 \
    --Speakers.0.NameTerms.0.Src Xiao Yan \
    --Speakers.0.NameTerms.0.Dst 萧炎
```

Output: 
```
{
    "Response": {
        "ProjectId": "458f16b1-7da9-4a56-a841-78567c5bee48",
        "RequestId": "28d958f5-86e5-4ccc-be23-77c87dc748f0"
    }
}
```

