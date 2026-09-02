**Example 1: 查询克隆音色**

查询克隆音色

Input: 

```
tccli vod DescribeVoices --cli-unfold-argument  \
    --SubAppId 260***028 \
    --VoiceType clone \
    --VoiceId v1_aBbiY3aN7tm7ff3S1gBZa************************plXzQDwNTiJQp2aYilZGv0=
```

Output: 
```
{
    "Response": {
        "Voices": [
            {
                "Age": "unknown",
                "AudioUrl": "",
                "Category": "clone",
                "Description": "克隆音色",
                "Gender": "male",
                "Labels": [
                    "磁性"
                ],
                "Languages": [
                    "zh"
                ],
                "Name": "克隆音色",
                "Scenes": [
                    "解说"
                ],
                "VoiceId": "v1_aBbiY3aN7tm7ff3S1gBZamsLQyEsQswXoEpreGEStjnx2plXzQDwNTiJQp2aYilZGv0="
            }
        ],
        "RequestId": "3e71a833-176c-418c-a515-c14a43b5f8b8"
    }
}
```

