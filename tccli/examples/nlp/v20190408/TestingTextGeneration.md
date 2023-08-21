**Example 1: 文案创作（内测版）**

文案创作（内测版）成功案例

Input: 

```
tccli nlp TestingTextGeneration --cli-unfold-argument  \
    --Model TestingModel \
    --QueryId 2121 \
    --Messages.0.Role system \
    --Messages.0.Content  \
    --Messages.1.Role user \
    --Messages.1.Content 天为什么是蓝的？ \
    --Temperature 1 \
    --TopP 1 \
    --TopK 40 \
    --RepetitionPenalty 1 \
    --OutputSeqLen 1 \
    --MaxInputSeqLen 1
```

Output: 
```
{
    "Response": {
        "RequestId": "246648dc-c6f6-4772-8db9-6d0cb6c716d6",
        "Choices": [
            {
                "Message": {
                    "Role": "assistant",
                    "Content": "天空为什么是蓝色的，这是一个非常有趣的问题！其实，这个现象主要是因为大气中气体和其他粒子对阳光的散射作用造成的。\n\n当阳光穿过大气层时，它会遇到许多气体分子和其他小颗粒。这些颗粒非常小，以至于它们能够将阳光中的不同颜色的光线散射到不同的方向。其中，蓝色光线的波长较短，因此比其他颜色的光线更容易被散射。\n\n当蓝色光线被散射时，它会沿着各个方向传播，最终到达我们的眼睛。这就是为什么我们看到的天空是蓝色的原因。然而，由于人眼对不同颜色的光线的敏感度不同，我们通常看不到蓝色光线被散射的最远距离。因此，当我们看到天空时，我们看到的是蓝色光线被散射到各个方向的光斑。\n\n总之，天空之所以是蓝色，是因为阳光中的蓝色光线在大气中被散射，而其他颜色的光线则相对较少地被散射。"
                }
            }
        ],
        "Created": 1692092667,
        "Id": "2121",
        "Model": "TestingModel",
        "Usage": {
            "PromptTokens": 7,
            "CompletionTokens": 185,
            "TotalTokens": 192
        }
    }
}
```

**Example 2: 文案创作（内测版）失败场景**

参数错误

Input: 

```
tccli nlp TestingTextGeneration --cli-unfold-argument  \
    --Model TestingModel \
    --QueryId 2121 \
    --Temperature 0 \
    --TopP 0 \
    --TopK 0 \
    --RepetitionPenalty 1 \
    --Messages.0.Role systemss \
    --Messages.1.Role user2 \
    --Messages.1.Content 天为什么是蓝的？ \
    --OutputSeqLen 1 \
    --MaxInputSeqLen 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "Messages.Role: systemss not in list: [system,user,assistant]"
        },
        "RequestId": "c625ff29-ab78-46cf-88f3-50041f69971d"
    }
}
```

**Example 3: 自我介绍文案生成**

自我介绍

Input: 

```
tccli nlp TestingTextGeneration --cli-unfold-argument  \
    --Model TestingModel \
    --QueryId 12122 \
    --Messages.0.Role system \
    --Messages.0.Content  \
    --Messages.1.Role user \
    --Messages.1.Content 帮我写个自我介绍 \
    --Messages.2.Role assistant \
    --Messages.2.Content 大家好，我叫小张，今年25岁，来自美丽的江南水乡苏州。我毕业于XX大学，专业是计算机科学与技术。在大学期间，我积极参加各类实践活动，培养了自己的团队协作和沟通能力。\n\n工作方面，我于去年加入了某互联网公司，作为一名软件工程师，负责公司项目的开发和维护工作。我擅长用Java、Python等编程语言进行软件开发，并熟悉MySQL等数据库技术。在团队中，我乐于分享经验，并积极参与讨论，以推动技术水平的不断提升。\n\n业余时间，我喜欢看书、打篮球和旅行。通过这些活动，我拓宽了自己的人生视野，也结交了许多志同道合的朋友。\n\n我希望在未来的工作中，能够不断学习和成长，为公司的发展做出贡献，也为个人价值的实现而不懈努力。谢谢大家！ \
    --Messages.3.Role user \
    --Messages.3.Content 我叫和先生，帮我写个自我介绍
```

Output: 
```
{
    "Response": {
        "Choices": [
            {
                "Message": {
                    "Content": "大家好，我叫和先生，来自中国北京。我毕业于清华大学，主修计算机科学专业。在学校期间，我一直努力学习新知识，积极参加各种实践活动，不断挑战自己。通过这些经历，我不仅锻炼了扎实的专业技能，也形成了较强的团队协作能力和分析解决问题的能力。\n\n工作方面，我曾加入一家顶尖的创业公司担任技术总监，负责开发和管理公司的多个项目。我对前端和后端开发都有着丰富的经验，熟悉Java、Python等多种编程语言。在团队里，我总是乐于分享自己的经验和见解，推动团队技术创新。\n\n业余时间，我喜欢户外运动、骑行和参加公益活动。这些活动让我保持健康的身体和良好的心态，也让我更加关心社会，培养自己的责任感和同理心。\n\n我很期待能够加入贵公司，发挥自己的专业知识和热情，为公司的发展贡献力量，同时也为自己的成长积累更多的经验。谢谢大家！",
                    "Role": "assistant"
                }
            }
        ],
        "Created": 1692102278,
        "Id": "12122",
        "Model": "TestingModel",
        "RequestId": "886975d4-f865-4db6-afb7-f2fcfa8d08a5",
        "Usage": {
            "CompletionTokens": 176,
            "PromptTokens": 173,
            "TotalTokens": 349
        }
    }
}
```

