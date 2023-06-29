**Example 1: 修改直播课**

该API用于修改直播课程名字和课程公开标记

Input: 

```
tccli tcop ModifyFastLiveCourse --cli-unfold-argument  \
    --IdaasOrgId tn-c65190017f394836863e83ca429b500c \
    --TermId 1000030510 \
    --VisibleScope 0 \
    --Name moon
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

