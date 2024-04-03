**Example 1: SOE初始化请求示例**



Input: 

```
tccli soe InitOralProcess --cli-unfold-argument  \
    --ScoreCoeff 1 \
    --TextMode 0 \
    --ServerType 0 \
    --SessionId 30716e3c-8cf2-452e-ab0f-f4cec2c36d3d \
    --RefText this \
    --WorkMode 0 \
    --EvalMode 1
```

Output: 
```
{
    "Response": {
        "RequestId": "923afe12-5c5e-4e42-914e-ae66d207ce2c",
        "SessionId": "30716e3c-8cf2-452e-ab0f-f4cec2c36d3d"
    }
}
```

**Example 2: 初始化发音评估过程**

初始化发音评估过程

Input: 

```
tccli soe InitOralProcess --cli-unfold-argument  \
    --SessionId stress_test_956938 \
    --ScoreCoeff 3.5 \
    --RefText again \
    --WorkMode 0 \
    --EvalMode 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxx",
        "SessionId": "xxxxxx"
    }
}
```

