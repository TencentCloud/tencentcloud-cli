**Example 1: 删除会话产物**

删除会话产物，如果 SessionId 存在，则删除 SessionId 对应会话内的所有产物，如果 ArtifactIds 有元素，会批量删除指定 ArtifactId 对应的产物记录。

Input: 

```
tccli workbuddyenterprise DeleteSessionArtifactList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "1364edc5-1428-4e03-8ada-517b4133a990"
    }
}
```

