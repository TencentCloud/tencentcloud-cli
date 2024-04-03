**Example 1: 正确返回**



Input: 

```
tccli tcop CreateFastLiveCourse --cli-unfold-argument  \
    --TeacherId 2007051 \
    --Name moon \
    --VisibleScope 0 \
    --IdaasOrgId tn-c65190017f394836863e83ca429b500c
```

Output: 
```
{
    "Response": {
        "TermId": "1000035819",
        "LiveUrl": "https://ke.qq.com/webcourse/1016064/1000035819#taid=245942713286912&lite=1",
        "RequestId": "e3362314-d89b-4f35-a3b4-e0bd0318d31d"
    }
}
```

**Example 2: 发布直播课**

该API用于为特定老师发布一门直播课

Input: 

```
tccli tcop CreateFastLiveCourse --cli-unfold-argument  \
    --IdaasOrgId tn-c65190017f394836863e83ca429b500c \
    --TeacherId 2007051 \
    --VisibleScope 0 \
    --Name moon
```

Output: 
```
{
    "Response": {
        "TermId": "100187514",
        "LiveUrl": "https://ke.qq.com/webcourse/100187514/1001875141#taid=1001875143&lite=1",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

