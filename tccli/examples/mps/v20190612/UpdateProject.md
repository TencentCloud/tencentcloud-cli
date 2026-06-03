**Example 1: 剧集项目更新**



Input: 

```
tccli mps UpdateProject --cli-unfold-argument  \
    --ProjectId 458f16b1-7da9-4a56-a841-78567c5bee48 \
    --ProjectName 斗破苍穹（第二季） \
    --TermBase.0.Src Canaan Academy \
    --TermBase.0.Dst 迦南学院 \
    --Description 玄幻题材有声剧第二季 \
    --Speakers.0.SpeakerId xiao_yan \
    --Speakers.0.VoiceId voice_001 \
    --Speakers.0.Gender male \
    --Speakers.0.Description 主角萧炎 \
    --Speakers.0.NameTerms.0.Src Xiao Yan \
    --Speakers.0.NameTerms.0.Dst 萧炎
```

Output: 
```
{
    "Response": {
        "RequestId": "0789fbea-b682-4719-ba5e-306bec1b4629"
    }
}
```

